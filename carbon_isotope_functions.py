import numpy as np

#############carbon_isotope_functions.py#############
#Hannah Zanowski
#7/24/20
#Houses various python functions useful for managing
#and interpreting carbon isotopes from C-iTRACE

#Compute model 14C age from abiotic D14C (Del14C)
def c14_age(D14C):
#D14C is the value of Delta 14C in per mil, an N-D array 
	c14age=-8033.0*np.log(1.0+(D14C/1000.0))
	return c14age

#Compute model 14C age from abiotic D14C (Del14C)
#Following Godwin 1962
def c14_age_godwin(D14C):
	c14age=-8267.0*np.log(1.0+(D14C/1000.0))
	return c14age


#Convert model biotic d14C (delta14C) to model D14C 
#(can then be used to compute 14C age above)
def d14c_to_D14C(d14C,d13C):
#d14C is the value of delta 14C in per mil, an N-D array
#d13C is the value of delta 13C in per mil, an N-D array
#that is the same size as d14C 
	D14C=d14C-2.0*(d13C+25.0)*(1.0+d14C/1000.0)
	return D14C
