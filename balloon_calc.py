#balloon_calc.py
from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree

class BalloonCalc(Component):
	"""calculate the cost/weight of the balloon"""
	#Inputs
	volume = Float(5000, iotype='in', desc='', units='m**3')
	#Constants
	thickness = Float(0.00002, desc='balloon thickness', units='m')
	#Outputs
	balloon_cost = Float(iotype='out', desc='', units='USD')
	balloon_weight = Float(iotype='out', desc='', units='kg')
	def execute(self):
		"""(This calculation is just a placeholder.)"""
		self.balloon_cost = 500
		self.balloon_weight = .1

