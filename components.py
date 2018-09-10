from copy import copy
import operator
from intelligence_unit import IntelligenceUnit



class Component:
    """
    The component class is as generic as possible. It encompasses the totpology of a network, each component
    having reference to its parents and children.
    It can also communicate to other components, reading from a buffer in.
    :attributes
        _id = the unique id of the component
        _children : a dictionary {int:Component} of the children, linking ids to the components
        _parents : a dictionary {int:Component} of the children, linking ids to the components
    """
    _id = -1
    _children = None
    _parents = None
    _buffer_out_feedback = None



    def __init__(self, *args, **kwargs):
        """
        :param args: id, TBD
            id |int| : the unique id number for this component
        :param kwargs: parents, children, TBD
            parents | dic<int,Component> | : dict of the parent components. Key is the id of the components
            children | dic<int,Component> | : dict of the child components. Key is the id of the components
        """
        if len(args) > 0:
            self._id = args[0]
        else:
            print("No id provided, things might go wrong.")
        self._parents = kwargs.get("parents", {})
        self._children = kwargs.get("children", {})


    def get_id(self):
        return copy(self._id)

    def get_children_list(self):
        """
        :return: the children of the component, as a list
        """
        ret = []
        for key in self._children.keys():
            ret.append(self._children[key])
        return ret


    def add_parent(self, parent):
        """
        Adds a parent to the component, and updates the children of the parent.
        :param parent:
        :return:
        """
        if not isinstance(parent, Component):
            raise TypeError("This methods expects a Component, not a " + type(parent).__name__)
        if parent.get_id() not in self._parents.keys():
            self._parents[parent.get_id()] = parent
            parent._children[self._id] = self
        else:
            print ("This component is already a parent.")

    def run(self):
        """
        Thi methods is launched at each tick, and should run all the logic of the component
        :return:
        """
        pass

    def get_feedback(self):
        """
        Returns a copy of the feedbacks from this component
        :return:
        """
        return copy(self._buffer_out_feedback)

    def gather_goals(self):
        """
        This method gathers the goals from above
        :return: a list of all the goals
        """
        goals = {}
        for key in self._parents.keys():
            goals[key] = self._parents[key].get_out_goal()
        return goals

    def get_parents_number(self):
        return len(self._parents)

    def __str__(self):
        return "( " + type(self).__name__ + ", id = " + str(self._id) + " )"

    def __repr__(self):
        # I know this is not very Pythonic but I don't care.
        return str(self)



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

    def malfunction(self, time):
        self.is_working = False
        self.failure_time_stamp = time

    def repair(self):
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
            # We recursively run the abduction on the children to see when they failed, and we later report the earliest
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


class AutonomicComponent(Component):
    """
    Extends the component class to a component able to process goals to produce sub-goals that will be transmitted to
    lower level components.
    """

    _buffer_goal_out = None

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def compute_goals(self, inputs):
        """
        This method should update the _buffer_goal_out variable.
        :return:
        """
        pass

    def gather_in_feedbacks(self):
        """
        :return: A dictionary { int : feedback } of the feedbacks from the children
        """
        feedbacks = {}
        for key in self._children.keys():
            feedbacks[key] = self._children[key].get_feedback()
        return feedbacks

    def get_out_goal(self):
        """
        Returns the goal stored in the buffer.
        :return:
        """
        return copy(self._buffer_goal_out)


class AutonomicIntelligentComponent(IntelligenceUnit, AutonomicComponent, PenetrableComponent):
    """
    This component is an intelligent controller capable of explaining what is wrong and
    performing reasoning to detect the malfunctioning child.
    """

    def __init__(self, *args, **kwargs):
        AutonomicComponent.__init__(self,*args,**kwargs)
        IntelligenceUnit.__init__(self,*args,**kwargs)
        PenetrableComponent.__init__(self,*args,**kwargs)

    def run(self):
        in_goals = self.gather_goals()
        self.compute_goals(in_goals)
        self.feed_inputs(self.gather_in_feedbacks())
        self.think()


