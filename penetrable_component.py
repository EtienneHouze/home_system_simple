from component import Component

import operator

class PenetrableComponent(Component):
    """
    This class is for components that can perform abduction to explain the cause of a
    potential failure
    :Attributes:
        - is_working : a boolean that is used to know if this component is working. When in the process of abduction,
            this attribute is used.
        - failure_time_stamp : when the component ceased to work
    """
    is_working = None
    failure_time_stamp = -1

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.is_working = True
        self.failure_time_stamp = -1

    def abduction(self):
        """
        This method performs the abduction
        :return: failing_component, time_of_failure
        """
        # We get the list of the penetrable children that fail too
        children_failing = {}
        for child in self.get_children_list():
            try:
                if not child.is_working:
                    children_failing[child] = child.failure_time_stamp
            except AttributeError:
                pass
        # if no child is found, that means this component is responsible, or that the lower levels are non penetrable
        if len(children_failing) == 0:
            if not self.is_working:
                return self,self.failure_time_stamp
            else:
                return None, None
        else:
            # We recursively run the abduction to the children to see when they failed, and we later report the earliest
            # detected failure.
            time_of_failure = None
            failing_component = None
            # Initialization at the current component and its timestamp
            if not self.is_working:
                failing_component = self
                time_of_failure = self.failure_time_stamp
            for child in children_failing.keys():
                comp, time_stamp = child.abduction()
                if time_of_failure is not None and time_stamp is not None:
                    if time_of_failure > time_stamp:
                        time_of_failure = time_stamp
                        failing_component = comp
                else:
                    time_of_failure = time_stamp
                    failing_component = comp
            return failing_component, time_of_failure
