from autonomic_intelligent_component import AutonomicIntelligentComponent
from penetrable_component import PenetrableComponent

import numpy as np


class Controller(AutonomicIntelligentComponent):

    def __init__(self,*args,**kwargs):
        super().__init__(args,kwargs)

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

    def think(self):
        pass


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
        self._buffer_out = self.report_temperature()

