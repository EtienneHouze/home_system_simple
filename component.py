from ai_system import AISystem

class Component:
    # TODO changing lists to dicts for inputs

    _id = -1                # id should be unique

    ai_system = None

    in_goal = None          # This field will be filled with a list of ndarray
                            # containing the goals sent to this component by its parents
    in_feedback = None      # Will contain the list of ndarrays, the feedback sent to this
                            # component by its children

    out_ai = None           # output of the AI module
    out_goal = None         # ndarray output buffer
    out_feedback = None     # ndarray output buffer

    _children = None
    _parents = None

    def function(self):
        """
        Must be overridden in implementations of this class

        This method should fill in the output fields, executing the logic we want to implement in the class
        """
        pass


    def __init__(self, fun=None, children=None, parents=None, id=-1):
        if fun is not None:
            self._function = fun
        if children is not None:
            self._children = children
        if parents is not None:
            self._parents = parents
        self._id = id
        self.in_feedback = {}
        self.in_goal = {}
        self.out_feedback = []
        self.out_goal = []
        self.ai_system = AISystem()

    def run(self):
        self.in_feedback = {}
        if len(self._parents) > 0:
            self.in_goal = {}
        for parent_id in self._parents.keys():
            self.in_goal[parent_id] = self._parents[parent_id].out_goal
        for child_id in self._children.keys():
            self.in_feedback[child_id] = self._children[child_id].out_feedback
        goals_list = []
        for key in self.in_goal.keys():
            goals_list.append(self.in_goal[key])
        feeds_list = []
        for key in self.in_feedback.keys():
            feeds_list.append(self.in_feedback[key])
        self.ai_system.feed_inputs([goals_list, feeds_list])
        self.function()
        self.ai_system.think()
        self.out_ai = self.ai_system.get_outputs()

    def get_id(self):
        return self._id

    def add_to_ctrl_system(self, ctrl):
        id = 0
        while id in ctrl.components.keys():
            id += 1
        self._id = id
        ctrl.components[id] = self

    def add_parent(self,parent):
        """
        Adds a component as a parent of this one. Also adds this to the children of the parent
        :param parent: Component object
        :return:
        """
        if parent.get_id() not in self._parents.keys():
            self._parents[parent.get_id()] = parent
            parent._children[self.get_id()] = self

    def add_child(self,child):
        if child.get_id() not in self._children.keys():
            self._children[child.get_id()] = child
            child._parents[self.get_id()] = self

    def __str__(self):
        children_str = ""
        for child in self._children:
            children_str += " " + type(child).__name__ + " " + str(child.get_id()) + " "
        return "Component " + type(self).__name__ + " " + str(self._id) + " with children " + children_str
