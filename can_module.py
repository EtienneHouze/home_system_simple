

class CANModule:
    """
    This class describes a module implementing the CAN thinking :
        - it can probe components with "spotlight" to find the cause of an anomaly
        - this module should be the only one in the system that can interact with the user
        to avoid a situation where every component tries to report activities to the user.
    """
    def __init__(self):
        pass

    def spotlight(self, component):
        """
        Used to probe the component to recursively find the cause of the anomaly
        :param component: (Component)
        :return:
        """
        try:
            return component.abduction()
        except AttributeError as e:
            print(e.__traceback__,e.args)
            print("The component has no penetrability")
