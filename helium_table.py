from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree

#http://openmdao.org/dev_docs/basics/variables.html#variable-trees
from openmdao.lib.datatypes.api import Array
from numpy import array
from numpy import float as numpy_float

#Helium Table (30,000 ft)
m =   Array(array([34,  70, 190,  370,  700, 1400,  2500]), dtype=numpy_float, desc='Max Liftable Weight', units='kg')
v = Array(array([100, 200, 500, 1000, 2000, 5000, 10000]), dtype=numpy_float, desc='Helium Volume', units='m**3')

#Helium Table (65,000 ft)
m2 =   Array(array([7.5,  15,   38,   75,  150,   380,   720,  1300,   2900]), dtype=numpy_float, desc='Max Liftable Weight', units='kg')
v2 = Array(array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]), dtype=numpy_float, desc='Helium Volume', units='m**3')

#Helium Table (100,000 ft)
m3 =   Array(array([  3,   8,   15,   30,   80,   150,   300,   800, 1500]), dtype=numpy_float, desc='Max Liftable Weight', units='kg')
v3 = Array(array([200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]), dtype=numpy_float, desc='Helium Volume', units='m**3')


#U.S Standard Atmosphere Air Properties (SI Units) 100,000ft = 30,480m
#http://www.engineeringtoolbox.com/standard-atmosphere-d_604.html
alt = Array(array([0,	1000,	2000,	3000,	4000,	5000,	6000,	7000,	8000,	9000,	10000,	15000,	20000,	25000,	30000,	40000,	50000,	60000,	70000,	80000]), dtype=numpy_float, desc='Altitude', units='m')
temp = Array(array([15,	8.5,	2,	-4.49,	-10.98,	-17.47,	-23.96,	-30.45,	-36.94,	-43.42,	-49.9,	-56.5,	-56.5,	-51.6,	-46.64,	-22.8,	-25,	-26.13,	-53.57,	-74.51]), dtype=numpy_float, desc='temp', units='degC')
g = Array(array([9.807,	9.804,	9.801,	9.797,	9.794,	9.791,	9.788,	9.785,	9.782,	9.779,	9.776,	9.761,	9.745,	9.73,	9.715,	9.684,	9.654,	9.624,	9.594,	9.564]), dtype=numpy_float, desc='acceleration due to gravity', units='m/s**2')
abs_pressure  = Array(array([10.13,	8.988,	7.95,	7.012,	6.166,	5.405,	4.722,	4.111,	3.565,	3.08,	2.65,	1.211,	0.5529,	0.2549,	0.1197,	0.0287,	0.007978,	0.002196,	0.00052,	0.00011]), dtype=numpy_float, desc='Absolute Pressure', units='(10**4)*N/m**2')
density = Array(array([12.25,	11.12,	10.07,	9.093,	8.194,	7.364,	6.601,	5.9,	5.258,	4.671,	4.135,	1.948,	0.8891,	0.4008,	0.1841,	0.03996,	0.01027,	0.003097,	0.0008283,	0.0001846]), dtype=numpy_float, desc='Density', units='(10**-1)*kg/m**3')
dyn_viscosity = Array(array([1.789,	1.758,	1.726,	1.694,	1.661,	1.628,	1.595,	1.561,	1.527,	1.493,	1.458,	1.422,	1.422,	1.448,	1.475,	1.601,	1.704,	1.584,	1.438,	1.321]), dtype=numpy_float, desc='Dynamic Viscosity', units='(10**-5)*N*s/m**2')

