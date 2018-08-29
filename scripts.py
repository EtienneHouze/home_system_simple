#   Example of a script building and running some components

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

from simple_system.component import Component
from simple_system.system import System
from simple_system.actuasensor import ActuaSensor
from simple_system.control_system import ControlSystem
from simple_system.ai_system import AISystem


#   We create three classes to implement each component
class Thermometer(ActuaSensor):
    delta = 1
    is_working = True
    temp_mem = -1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "delta" in kwargs.keys():
            self.delta = kwargs["delta"]

    # Overriding of the function
    def function(self):
        coinflip = np.random.uniform()
        if coinflip > 0.99:
            self.is_working = not self.is_working
        if self.is_working:
            new_temp = np.random.normal(self.system.get_temp(), self.delta, 1)
            self.out_feedback = [new_temp, self.temp_mem - new_temp]
            self.temp_mem = new_temp
        else:
            new_temp = max(0,np.random.normal(self.system.get_temp(), 200, 1))
            self.out_feedback = [new_temp, self.temp_mem - new_temp]
            self.temp_mem = new_temp
        # TODO : case where the component is not working properly


class Heater(ActuaSensor):
    """
    Class representing a heater.
    As an actuator, the heater should not have any children, and can affect the room.
    Its inputs are binary, a command whether to work or not.
    """

    is_heating = False
    cold_temp = 18
    hot_temp = 25

    power_consumption = 0  # power consumption of the heater TODO use it

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def function(self):
        # Expect that the goal is 1D, 1-element array
        if self.in_goal is None:
            self.system.set_temp(15)
            self.out_feedback = 0
        elif len(self.in_goal) == 0:
            self.system.set_temp(15)
            self.out_feedback = 0
        elif self.in_goal[0] is None:
            self.system.set_temp(15)
            self.out_feedback = 0
        elif self.in_goal[0] > 0:  # heat the room
            self.system.set_temp(23)
            self.out_feedback = 1
        else:
            self.system.set_temp(15)
            self.out_feedback = 0
        self.out_feedback = [self.out_feedback]


class Controller(Component):
    # The controller inputs are :
    #   feedback : a list of values from the thermometers and heaters
    #   goals : a binary value coding whether to heat up or not.

    class ControllerAi(AISystem):
        # The inputs of this module are [in_goals, in_feedback] of the controller

        def __init__(self):
            super().__init__()

        def think(self):
            # TODO import here the logic of the AI
            is_outlier = self.discriminate()

        def discriminate(self):
            num_inputs = len(self._inputs)
            heater_on = False
            max_temp = -1000
            min_temp = 1000
            goal = self._inputs[0]
            feeds = self._inputs[1]
            heater_on = 0       # feedback from the heater
            temps_feeds = []    # feedback from the thermometers
            for feed in feeds:
                if len(feed) == 0:
                    pass
                elif feed[0] == 1 or feed[0] == 0:
                    heater_on = feed[0]
                else:
                    temps_feeds.append(feed)
            if heater_on != goal[0]:
                print("Problem detected : Heater malfunction")
            for therm in temps_feeds:
                measured_temp = therm[0][0]
                print(measured_temp)
                if not 15 < measured_temp < 25:
                    print("Problem detected : temperature is out of bound for the room")

        def explain(self):
            super().explain()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ai_system = Controller.ControllerAi()

    def function(self):
        # Pass on the orders to the lower levels
        self.out_goal = None
        if self.in_goal is None:
            pass
        elif len(self.in_goal) == 0:
            pass
        elif self.in_goal[0] > 0:
            self.out_goal = 1
        else:
            self.out_goal = 0
        # process the feedbacks from below
        if len(self.in_feedback) == 0:
            pass
        else:
            for i in range(len(self.in_feedback)):
                #print("feedback for " + str(self._children[i].get_id()) + " is " + str(self.in_feedback[i]))
                pass


#   A method to build a system with a controller, two thermometers and a heater
def build_system():
    house = System()
    t1 = Thermometer(system=house,delta=0.1)
    t2 = Thermometer(system=house, delta=0.1)
    h = Heater(system=house)
    test = Controller()
    test._parents = []
    test._children = []
    test.add_child(t1)
    test.add_child(t2)
    h.add_parent(test)
    system = ControlSystem()
    t1.add_to_ctrl_system(system)
    t2.add_to_ctrl_system(system)
    test.add_to_ctrl_system(system)
    h.add_to_ctrl_system(system)
    system.find_root()
    return system


def main():

    system = build_system()
    hour = 0
    i = 0

    while i < 200:
        user_will = [1] * 24
        system.run(user_will[hour])
        i += 1
        hour = i % 24
        print ("cycle : " + str(i))
        user_input = input("Continue ? (y/n)")
        if user_input != "y" and user_input != "Y":
            break


if __name__ == "__main__":
    main()
