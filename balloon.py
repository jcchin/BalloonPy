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
    volume = Float(5000, desc='', units='m**3')


    mass = Float(200, iotype='in', desc='Payload Mass', units='kg', low=150, high=220)     
    max_alt = Float(100, iotype='in', desc='Desired Max Altitude', low=0, high=220)
    max_rise_time = Float(24, iotype='h', desc='Maximum balloon rise time')

    #GHAPS Constants

    def configure(self):

        #Add Components
        self.add('GHAPS', GHAPS())
        self.add('NASA_Fly', NASA_Fly())
        self.add('GasCalc', GasCalc())
        self.add('BalloonCalc', GasCalc())

        #Component Connections
        #GHAPS -> NASA_Fly
        self.connect('GHAPS.v_terminal', 'NASA_Fly.v_terminal')
        #NASA_Fly -> GasCalc
        self.connect('NASA_Fly.mass','GasCalc.payload_mass')
        #GasCalc -> BalloonCalc
        self.connect('GasCalc.gas_vol','BallCalc.vol')
        #Feedback
        #BalloonCalc -> GasCalc
        #self.connect('BallCalc.balloon_mass','GasCalc.balloon_mass')

        #Add Solver
        solver = self.add('solver',BroydenSolver())
        solver.itmax = 50 #max iterations
        solver.tol = .001
        #Add Parameters and Constraints
        solver.add_parameter(['NASA_Fly.balloon_mass','BallCalc.balloon_mass'], low=-1e-15, high=1e15)
        solver.add_parameter(['NASA_Fly.balloon_mass', 'pod.radius_tube_inner'], low=-1e15, high=1e15)

        driver = self.driver
        driver.workflow.add('solver')
        
        #Declare Solver Workflow
        solver.workflow.add(['GHAPS','NASA_Fly','GasCalc','BallCalc'])

if __name__=="__main__": 
    import numpy as np

    b = Balloon()
    
    b.run()
    #design variables
    #hl.Mach_bypass = .95
    
    print "======================"
    print "Using Helium @", 1000, "ft, for a 24hr rise time"
    print "Volume Required:", b.volume
    print "Gas Cost", b.cost
    print "Balloon Cost", b.b_cost
    print "----------------------"
    print "Payload Area: ", b.area
    print "Payload Terminal Velocity: ", b.v_terminal
    

