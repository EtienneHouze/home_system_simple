from component import Component

from copy import copy


class AutonomicComponent(Component):
    """
    Extends the component class to a component able to process goals to produce sub-goals that will be transmitted to
    lower level components.
    """

    _buffer_goal_out = None

    def __init__(self):
        super().__init__()

    def compute_goals(self):
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