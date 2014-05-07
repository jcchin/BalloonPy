from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree

from numpy import interp
import helium_table

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
GHAPS = VarTree(Vehicle(), iotype='in')
GHAPS.mass = 450
GHAPS.area = 25
GHAPS.c_d = 0.8

class GHAPS(Component):
	""" Determine GHAPS terminal velocity"""
	g = interp(0, alt, g) #find g at sea level
    rho = interp(0, alt, density)#find rho_air at sea level
	#	Force Drag = 1/2*rho*(v**2)*c_d*area
	#	Weight = g*mass
	#	Weight = Drag <--- Terminal Velocity
	#	g*mass = 1/2*rho*(v_terminal**2)*c_d*area
	#	v_terminal = 2*g*mass/rho*cd*area
	v_terminal = 2*g*mass/rho*cd*area

#NASA Fly
class NASA_Fly(Component):
    """ Based on mass and GHAPS terminal velocity, calculates required payload base side length"""

    mass = Float(iotype='in', desc='payload mass', units='kg')
    v_terminal = Float(iotype='in', desc='terminal velocity', units='m/s')


    def execute(self):
    	g = interp(0, alt, g) #find g at sea level
    	rho = interp(0, alt, density)
	    #	Force Drag = 1/2*rho*(v**2)*c_d*area
		#	Weight = g*mass
		#	Weight = Drag <--- Terminal Velocity
		#	g*mass = 1/2*rho*(v_terminal**2)*c_d*area
		#   area = 2*g*mass/rho*(v_terminal**2)*c_d
		area = 2*g*mass/rho*(v_terminal**2)*c_d
		side_len = area**2