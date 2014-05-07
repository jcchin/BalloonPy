#gas_calc.py
from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree
from numpy import interp

from gas_library import hydrogen, helium
from helium_table import *

class GasCalc(Component):
	"""calculate the amount of gas necessary to lift balloon"""
	#Inputs
	payload_mass = Float(iotype='in', desc='', units='kg')
	
	#Constants
	balloon_weight = Float(1, desc='balloon weight', units='kg')
	#Outputs
	estimate_weight = Float(iotype='out', desc='', units='kg')
	volume = Float(iotype='out', desc='', units='m**3')
	gas_cost = Float(iotype='out', desc='', units='USD')
	gas_weight = Float(iotype='out', desc='', units='kg')

	def execute(self):
		#mass = self.payload_mass #normal interpolation
		mass = min(m3, key=lambda x:x-self.payload_mass if x-self.payload_mass> 0 else 9999) #round up to nearest table point
		#mass = min(m, key=lambda x:abs(x-self.payload_mass)) #round up to nearest table point
		self.estimate_weight = mass

		self.volume = interp(mass, m3, v3)
		self.gas_cost = self.volume * helium.cost
		self.gas_weight = self.volume * helium.rho_stp

		print self.payload_mass
		print mass
		print self.volume
