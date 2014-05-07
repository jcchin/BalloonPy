#import openMDAO functionality
from openmdao.main.api import Assembly, Component, VariableTree
from openmdao.lib.datatypes.api import Float, Int, Str, VarTree

from openmdao.main.api import convert_units as cu

#import local files
from gas_library import Gas, helium, hydrogen
from payload_library import *
from helium_table import *

class Balloon(Assembly):
    #Inputs

	#Design Variables  
    mass = Float(200, iotype='in', desc='Payload Mass', units='kg', low=150, high=220)     
    max_alt = Float(100, iotype='in', desc='Desired Max Altitude', low=0, high=220)
    max_rise_time = Float(24, iotype='h', desc='Maximum balloon rise time')

    #GHAPS Constants

    #def configure(self):

        #Add Components
        #compress = self.add('compress', CompressionSystem())

        #Boundary Input Connections
        #Hyperloop -> Compress
        #self.connect('Mach_pod_max', 'compress.Mach_pod_max')
        

        #Add Solver
        #solver = self.add('solver',BroydenSolver())
        #solver.itmax = 50 #max iterations
        #solver.tol = .001
        #Add Parameters and Constraints
        #solver.add_parameter('compress.W_in',low=-1e15,high=1e15)

        #solver.add_parameter(['compress.Ts_tube','flow_limit.Ts_tube','tube_wall_temp.temp_boundary'], low=-1e-15, high=1e15)
        #solver.add_parameter(['flow_limit.radius_tube', 'pod.radius_tube_inner'], low=-1e15, high=1e15)

        #driver = self.driver
        #driver.workflow.add('solver')
        
        #Declare Solver Workflow
        #solver.workflow.add(['compress','mission','pod','flow_limit','tube_wall_temp'])

if __name__=="__main__": 
    import numpy as np

    b = Balloon()
    
    b.run()
    #design variables
    #hl.Mach_bypass = .95
    
    print "======================"
    print "Design"
    print "======================"
    print helium.cost


    print "======================"
    print "Performance"
    print "======================"
    

