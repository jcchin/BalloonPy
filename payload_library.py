#payload_library.py
#This file defines the GHAPS and NASA_Fly payloads
#Computes GHAPS terminal velocity, then backtracks to find necessary NASA_Fly geometry to match
from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree
from numpy import interp
import numpy as np
from scipy import interpolate

from helium_table import alt, g, density

#GHAPS
class GHAPS(Component):
	""" Determine GHAPS terminal velocity"""
	#Inputs (none)
	#Outputs
	v_terminal = Float(450, iotype='out', desc='terminal velocity', units='m/s')
	#Constants
	mass = Float(450, desc='payload mass', units='kg')
	area = Float(25, desc='aero cross-sectional area, assuming it\'s a cube', units='m**2')
	c_d = Float(0.8, desc='Approximate Coefficient of Drag')

	def execute(self):
		gee = interp(5000, alt, g) #find g at 5000m
		rho = interp(5000, alt, density)#find rho_air 5000m
		#	Force Drag = 1/2*rho*(v**2)*c_d*area
		#	Weight = g*mass
		#	Weight = Drag <--- Terminal Velocity
		#	g*mass = 1/2*rho*(v_terminal**2)*c_d*area
		#	v_terminal = 2*g*mass/rho*cd*area
		self.v_terminal = (2*gee*self.mass/(rho*self.c_d*self.area))**0.5

#NASA Fly
class NASA_Fly(Component):
	""" Based on mass and GHAPS terminal velocity, calculates required payload base side length"""
	#Inputs
	mass = Float(iotype='in', desc='payload mass', units='kg')
	v_terminal = Float(iotype='in', desc='terminal velocity', units='m/s')
	#Outputs
	area = Float(iotype='out', desc='aero cross-sectional area, assuming it\'s a cube', units='m**2')
	side_len = Float(iotype='out', desc='aero cross-sectional area, assuming it\'s a cube', units='m')
	#Constants
	c_d = Float(0.8, desc='Approximate Coefficient of Drag')

	def execute(self):
		gee = interp(5000, alt, g) #find g at sea level
		rho = interp(5000, alt, density)
		#	Force Drag = 1/2*rho*(v**2)*c_d*area
		#	Weight = g*mass
		#	Weight = Drag <--- Terminal Velocity
		#	g*mass = 1/2*rho*(v_terminal**2)*c_d*area
		#   area = 2*g*mass/rho*(v_terminal**2)*c_d
		self.area = 2*gee*self.mass/(rho*(self.v_terminal**2)*self.c_d)
		self.side_len = self.area**0.5