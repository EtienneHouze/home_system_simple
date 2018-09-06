from intelligence_unit import IntelligenceUnit
from autonomic_component import AutonomicComponent


class AutonomicIntelligentComponent(IntelligenceUnit, AutonomicComponent):
    """
    This component is an intelligent controller capable of explaining what is wrong and
    performing reasoning to detect the malfunctioning child.
    """

    def __init__(self, *args, **kwargs):
        pass

    def run(self):
        in_goals = self.gather_goals()
        self.compute_goals(in_goals)
        self.feed_inputs(self.gather_in_feedbacks())
        self.think()
        if self._ai_outputs == 0:
            # in this case it doesn't work
            pass
        else:
            # in this case it does
            pass


