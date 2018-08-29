from copy import copy

class System:
    """
        This class describes the system (house). It should interact only with the lower-level actuators and sensors.
    """

    _current_temp = 23

    def __init__(self):
        pass

    def get_temp(self):
        return copy(self._current_temp)

    def set_temp(self,temp):
        self._current_temp = temp
