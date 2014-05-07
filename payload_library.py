from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree

#Variable Tree definition
class Vehicle(VariableTree):
	#default GHAPS Constants
	mass = Float(450, desc='payload mass', units='kg')
	#rho = Float(0.1664, desc='air density at 5,000m', units='kg/m**3')
	
	#Assumed Cube (base area is a side length square), and Cd=0.8 for cube
	area = Float(25, desc='aero cross-sectional area, assuming it\'s a cube', units='m**2')
	c_d = Float(0.8, desc='Approximate Coefficient of Drag')




#Library Values

#GHAPS
GHAPS = VarTree(Gas(), iotype='in')
GHAPS.mass = 450
GHAPS.area = 25
GHAPS.c_d = 0.8



#	Force Drag = 1/2*rho*(v**2)*c_d*area
#	Weight = g*mass
#	Weight = Drag <--- Terminal Velocity
#	g*mass = 1/2*rho*(v_terminal**2)*c_d*area
#	v_terminal = 2*g*mass/rho*cd*area
v_terminal = 2*g*mass/rho*cd*area