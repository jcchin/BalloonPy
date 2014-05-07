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
	thickness = Float(0.00002, desc='balloon thickness', units='m')
	#Outputs
	volume = Float(iotype='in', desc='', units='m**3')
	gas_cost = Float(iotype='out', desc='', units='USD')
	gas_weight = Float(iotype='out', desc='', units='kg')

	def execute(self):
		#mass = self.payload_mass #normal interpolation
		mass = min(m, key=lambda x:x-self.payload_mass if x-self.payload_mass> 0 else 9999) #round up to nearest table point
		#mass = min(m, key=lambda x:abs(x-self.payload_mass)) #round up to nearest table point

		self.volume = interp(mass, m, v)
		self.gas_cost = self.volume * helium.cost
		self.gas_weight = self.volume * helium.rho_stp

		print self.payload_mass
		print mass
		print self.volume
