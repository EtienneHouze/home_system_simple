from copy import copy

class System:
    """
        This class describes the system (house). It should interact only with the lower-level actuators and sensors.
        Fields:
            _current_temp : the inside temperature of the house
    """

    _current_temp = 23

    def __init__(self):
        pass

    def get_temp(self):
        """
        :return: The current temperature of the room
        """
        return copy(self._current_temp)

    def set_temp(self,temp):
        """
        Sets the temperature of the room
        :param temp: a number (float or int)
        :return: nothing
        """
        if not (isinstance(temp,float) or isinstance(temp,int)):
            print("Temp should be a number, float or int")
        else:
            self._current_temp = temp
