from intelligence_unit import IntelligenceUnit
from autonomic_component import AutonomicComponent


class AutonomicIntelligentComponent(IntelligenceUnit, AutonomicComponent):
    """
    This component is an intelligent controller capable of explaining what is wrong and
    performing reasoning to detect the malfunctioning child.
    """

    def __init__(self, *args, **kwargs):
        pass
