from autonomic_intelligent_component import AutonomicIntelligentComponent
from penetrable_component import PenetrableComponent

import numpy as np


class Controller(AutonomicIntelligentComponent):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def compute_goals(self):
        """
        The goal form this component is either 1 ( should heat the room) or 0 (should not heat the room)
        :return
        """
        in_goals = self.gather_goals()
        main_goal = 0
        if len(in_goals) > 1 or len(in_goals) == 0:
            print("The goals are not what they are expected to be.")
        for key in in_goals.keys():
            main_goal = in_goals[key]
        if main_goal > 0:
            self._buffer_goal_out = 1
        else:
            self._buffer_goal_out = 0


    def run(self):
        self.compute_goals()
        feedbacks = self.gather_in_feedbacks()
        self.feed_inputs(feedbacks)
        self.think()
        if self._outputs > 0:
            return 1

    def think(self):
        self._outputs = 0
        temps_report = []
        for key in self._inputs.keys():
            if self._inputs[key] is not None:
                temps_report.append(self._inputs[key])
        for temp in temps_report:
            if temp < 15:
                self._description = "Too cold"
                self._outputs = 1
            if temp > 28:
                self._description = "Too hot"
                self._outputs = 1
        if self._outputs != 0:
            return
        self._outputs = 0


class Thermometer(PenetrableComponent):
    """
    Description of a thermometer
    """
    _house = None
    _deviation = 1.0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "house" in kwargs.keys():
            self._house = kwargs["house"]
        else:
            print("No house provided, behaviour will not be correct")
        self._deviation = kwargs.get("dev",1.0)

    def report_temperature(self):
        return np.random.normal(self._house.get_temp(),self._deviation)

    def run(self):
        if self.is_working:
            self._buffer_out = self.report_temperature()
        else:
            # return a totally random value if the thermometer is not working
            return np.random.normal(20,300)




class Heater(PenetrableComponent):
    """
    Description of a heater
    """
    _house = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        if "house" in kwargs.keys():
            self._house = kwargs["house"]
        else:
            print("No house provided, behaviour will no be correct")

    def heat(self):
        if self._house.get_temp() < 25:
            self._house.set_temp(self._house.get_temp() + 1)

    def cool(self):
        self._house.set_temp(self._house.get_temp() - 1)


    def run(self):
        # The heater heats the room if it is working and is asked to heat (goal == 1)
        if self.is_working:
            goals = self.gather_goals()
            if len(goals) == 0:
                self.cool()
            elif goals[0] > 0:
                self.heat()
            else:
                self.cool()
        else:
            self.cool()
