from copy import copy


class Component:
    """
    The component class is as generic as possible. It encompasses the totpology of a network, each component
    having reference to its parents and children.
    It can also communicate to other components, reading from a buffer in.
    :attributes
        _id = the unique id of the component
        _children : a dictionary {int:Component} of the children, linking ids to the components
        _parents : a dictionary {int:Component} of the children, linking ids to the components
        _buffer_in : the buffer for inputs coming to this component
    """
    _id = -1
    _children = None
    _parents = None
    _buffer_in = None
    _buffer_out = None



    def __init__(self, *args, **kwargs):
        """
        :param args: id, TBD
            id |int| : the unique id number for this component
        :param kwargs: parents, children
            parents | dic<int,Component> | : dict of the parent components. Key is the id of the components
            children | dic<int,Component> | : dict of the child components. Key is the id of the components
        """
        if len(args) > 0:
            self._id = args[0]
        self._parents = kwargs.get("parents", {})
        self._children = kwargs.get("children", {})

    def get_id(self):
        return self._id

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
        return copy(self._buffer_out)

    def gather_goals(self):
        """
        This method gathers the goals from above
        :return: a list of all the goals
        """
        goals = {}
        for key in self._parents.keys():
            goals[key] = self._parents[key].get_out_goal()
        return goals

    def __str__(self):
        return "( " + type(self).__name__ + ", id = " + str(self._id) + " )"