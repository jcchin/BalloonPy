from openmdao.main.api import Component, VariableTree
from openmdao.lib.datatypes.api import Float, VarTree

#Variable Tree definition
class Gas(VariableTree):
	#default to helium
	cost = Float(6.452, desc='Cost in $USD, #/m^3, NASA Praxair Quote', units='USD/m**3')
	rho_stp = Float(0.1664, desc='density at Standard TP 273.15 and 1 atm', units='kg/m**3')
	rho_ntp = Float(0.1786, desc='density at Normal TP 293.15 K and 1 atm', units='kg/m**3')




#Library Values
#http://www.engineeringtoolbox.com/gas-density-d_158.html

#Helium
helium = VarTree(Gas(), iotype='in')
helium.cost = 6.452
helium.rho_ntp = 0.1664
helium.rho_stp = 0.1786
#Hydrogen
hydrogen = VarTree(Gas(), iotype='in')
hydrogen.cost = 1.14
hydrogen.rho_ntp = 0.0899
hydrogen.rho_stp = 0.0899
#Air
air = VarTree(Gas(), iotype='in')
air.cost = 0
air.rho_ntp = 1.205
air.rho_stp = 1.293

