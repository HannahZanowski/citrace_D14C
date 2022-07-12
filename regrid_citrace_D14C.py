import xarray as xr
import numpy as np
import xesmf as xe
import cftime

########regrid_3d_with_xesmf.py############
#Script to regrid citrace 3d ocean variables using xesmf
#to run: python regrid_3d_with_xesmf.py

#Get the output
var='ABIO_D14Cocn'
wrk_direc='/glade/work/zanowski/citrace/'
xdo=xr.open_dataset(wrk_direc+'ctrace.decadal.'+var+'.nc')
sst=xdo[var]
#leftover from ncks
#Rename TLAT and TLONG to be lat and lon so xesmf knows that
#these are your lat/lon grids
#gotta change these if not on the tracer grid
sst=sst.rename({'TLAT':'lat','TLONG':'lon'})

#Regridding parameters
method='bilinear' #for conservative you need lat and lon bounds
#Reuse weights 
rw=False

#Define the target grid (the new grid you want your output on),
#in this case 2.5 deg lat x 3.5 deg lon
#Can also use xe.util.grid_global(xstride,ystride)
#will give lat and lon bounds as well
xstride=1.0 #2.0
ystride=1.0 #2.5
lat=np.arange(-89.5,89.6,ystride)
lon=np.arange(0.5,359.6,xstride)

#xstride=2.0
#ystride=2.5
#lat=np.arange(-90,90.1,ystride) #Whole globe, but do not include 90N otherwise
#lon=np.arange(0.0,361.0,xstride) #cartopy gets rage-y (i.e. it doesn't work) when plotting
lon2d,lat2d=np.meshgrid(lon,lat)
target_grid=xr.Dataset({'lat': (['y', 'x'], lat2d),'lon': (['y', 'x'], lon2d)})

#Set up the regridder
#NOTE: Once you have the output of this (the weight file), 
#you can set reuse_weights=True so that you don't need to
#recreate the weight file
regridder = xe.Regridder(sst, target_grid, method, periodic=True,reuse_weights=rw)
#Regrid
sst_rg = regridder(sst)

#If you want to save it as a netCDF, xarray has a nice way of doing this
#This is just a simple example
#Make the time variable because xarray has trouble saving the times
#that are all wonky in the original file
t2=np.array([cftime.DatetimeNoLeap(i, 7, 16, 22, 0, 0, 0, 0, 197) for i in range(1,22001,10)])
#also adjust depth to be in m, not cm
depth_m=0.01*np.array(xdo['z_t'])
ds=xr.Dataset()
ds[var]=(('time','z','y','x'),sst_rg)
ds.coords['lat']=(('y','x'), sst_rg['lat'])
ds.coords['lon']=(('y','x'),sst_rg['lon'])
ds.coords['z_t']=(('z'),depth_m)
ds.coords['time']=(('time'),t2)

#Add whatever attributes you want to document your output
ds['z_t'].attrs['long_name']=xdo['z_t'].attrs['long_name']
ds['z_t'].attrs['units']='meters'
ds['z_t'].attrs['positive']=xdo['z_t'].attrs['positive']
ds[var].attrs['long_name']=xdo[var].attrs['long_name']
ds[var].attrs['units']=xdo[var].attrs['units']
ds.attrs['Description']='citrace '+var+' regridded onto a rectilinear '+str('%.1f' %ystride)+'deg lat x '+str('%.1f' %xstride)+'deg lon grid'
#Set the missing and fill values to whatever they are in the original data
ds[var].encoding['_FillValue']=xdo[var].encoding['_FillValue']
ds[var].encoding['missing_value']=xdo[var].encoding['missing_value']
ds.to_netcdf(path=wrk_direc+'ctrace_'+var+'_decadal_'+method+'_regrid_'+str('%.1f' %ystride)+'x'+str('%.1f' %xstride)+'.nc')


