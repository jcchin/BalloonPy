#helium_table.py
#This file defines helium tables and atmospheric profile information for other calculations.
from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree #http://openmdao.org/dev_docs/basics/variables.html#variable-trees
from openmdao.lib.datatypes.api import Array
from numpy import array
from numpy import float as numpy_float


#Helium Table (30,000 ft)
m =   array([34,  70, 190,  370,  700, 1400,  2500], dtype=numpy_float) #, desc='Max Liftable Weight', units='kg'
v = array([100, 200, 500, 1000, 2000, 5000, 10000], dtype=numpy_float) #, desc='Helium Volume', units='m**3')

#Helium Table (65,000 ft)
m2 =   array([7.5,  15,   38,   75,  150,   380,   720,  1300,   2900], dtype=numpy_float) #, desc='Max Liftable Weight', units='kg')
v2 = array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000], dtype=numpy_float) #, desc='Helium Volume', units='m**3')

#Helium Table (100,000 ft)
m3 =   array([  3,   8,   15,   30,   80,   150,   300,   800, 1500], dtype=numpy_float) #, desc='Max Liftable Weight', units='kg')
v3 = array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000], dtype=numpy_float) #, desc='Helium Volume', units='m**3')

#U.S Standard Atmosphere Air Properties (SI Units) 100,000ft = 30,480m
#http://www.engineeringtoolbox.com/standard-atmosphere-d_604.html
alt = array([0,	1000,	2000,	3000,	4000,	5000,	6000,	7000,	8000,	9000,	10000,	15000,	20000,	25000,	30000,	40000,	50000,	60000,	70000,	80000], dtype=numpy_float) #, desc='Altitude', units='m')
temp = array([15,	8.5,	2,	-4.49,	-10.98,	-17.47,	-23.96,	-30.45,	-36.94,	-43.42,	-49.9,	-56.5,	-56.5,	-51.6,	-46.64,	-22.8,	-25,	-26.13,	-53.57,	-74.51], dtype=numpy_float) #, desc='temp', units='degC')
g = array([9.807,	9.804,	9.801,	9.797,	9.794,	9.791,	9.788,	9.785,	9.782,	9.779,	9.776,	9.761,	9.745,	9.73,	9.715,	9.684,	9.654,	9.624,	9.594,	9.564], dtype=numpy_float) #, desc='acceleration due to gravity', units='m/s**2')
abs_pressure  = array([10.13,	8.988,	7.95,	7.012,	6.166,	5.405,	4.722,	4.111,	3.565,	3.08,	2.65,	1.211,	0.5529,	0.2549,	0.1197,	0.0287,	0.007978,	0.002196,	0.00052,	0.00011], dtype=numpy_float)*(10**4) #, desc='Absolute Pressure', units='N/m**2')
density = array([1.225,	1.112,	1.007,	.9093,	.8194,	.7364,	.6601,	.59,	.5258,	.4671,	.4135,	.1948,	.08891,	.04008,	.01841,	.003996,	.001027,	.0003097,	.00008283,	.00001846], dtype=numpy_float) #, desc='Density', units='kg/m**3')
dyn_viscosity = array([.00001789,	.00001758,	.00001726,	.00001694,	.00001661,	.00001628,	.00001595,	.00001561,	.00001527,	.00001493,	.00001458,	.00001422,	.00001422,	.00001448,	.00001475,	.00001601,	.00001704,	.00001584,	.00001438,	.00001321], dtype=numpy_float) #, desc='Dynamic Viscosity', units='N*s/m**2')

