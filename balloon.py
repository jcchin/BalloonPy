#import openMDAO functionality
from openmdao.main.api import Assembly, Component, VariableTree
from openmdao.lib.datatypes.api import Float, Int, Str, VarTree
from openmdao.lib.drivers.api import BroydenSolver
from openmdao.main.api import convert_units as cu

#import local files
from gas_library import Gas, helium, hydrogen
from payload_library import *
from helium_table import *
from balloon_calc import *
from gas_calc import *

class Balloon(Assembly):
    #Inputs
    payload_mass = Float(200, iotype='in', desc='Payload Mass', units='lb')

	#Design Variables  
    volume = Float(5000, desc='', units='m**3')
         
    max_alt = Float(100, iotype='in', desc='Desired Max Altitude', low=0, high=220)
    max_rise_time = Float(24, iotype='h', desc='Maximum balloon rise time')

    #GHAPS Constants

    def configure(self):

        #Add Components
        self.add('GHAPS', GHAPS())
        self.add('NASA_Fly', NASA_Fly())
        self.add('GasCalc', GasCalc())
        self.add('BalloonCalc', BalloonCalc())
        #self.add('Ascent', Ascent())

        #-----------Component Connections-----------#
        #Top level connections
        self.connect('payload_mass', 'NASA_Fly.mass')
        self.connect('payload_mass','GasCalc.payload_mass')

        #InterComponent Connections
        #GHAPS -> NASA_Fly
        self.connect('GHAPS.v_terminal', 'NASA_Fly.v_terminal')
        #GasCalc -> BalloonCalc
        #self.connect('GasCalc.gas_vol','BallCalc.volume')
        #Feedback
        #BalloonCalc -> GasCalc
        #self.connect('BallCalc.balloon_mass','GasCalc.balloon_mass')

        #-----------Solver and Driver-----------#
        solver = self.add('solver',BroydenSolver())
        solver.itmax = 50 #max iterations
        solver.tol = .001
        #Add Parameters and Constraints
        #solver.add_parameter(['NASA_Fly.balloon_mass','BallCalc.balloon_mass'], low=-1e-15, high=1e15)
        #solver.add_parameter(['NASA_Fly.balloon_mass', 'pod.radius_tube_inner'], low=-1e15, high=1e15)

        driver = self.driver
        driver.workflow.add('solver')
        
        #Declare Solver Workflow
        solver.workflow.add(['GHAPS','NASA_Fly','GasCalc'])#,'BallCalc','Ascent'])

if __name__=="__main__": 
    import numpy as np

    b = Balloon() 
    b.run()
    
    print "======================"
    print "Using Helium @", 1000, "ft, for a 24hr rise time"
    print "Volume Required:", b.GasCalc.volume, "m^3"
    print "Gas Cost $", b.GasCalc.gas_cost, "for ", b.GasCalc.estimate_weight, "kg"
    print "Gas Weight ", b.GasCalc.gas_weight, "kg"
    print "Total Weight ", b.GasCalc.gas_weight + b.NASA_Fly.mass, "kg"
    #print "Balloon Cost", b.b_cost
    print "----------------------"
    #print "Payload Area: ", b.area
    print "Payload Terminal Velocity: ", b.GHAPS.v_terminal
    

