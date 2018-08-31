

class IntelligenceUnit:
    """
    An abstract class describing an intelligence unit
    """

    _inputs = None
    _outputs = None

    def __init__(self):
        pass

    def feed_inputs(self, inputs):
        self._inputs = inputs

    def think(self):
        pass