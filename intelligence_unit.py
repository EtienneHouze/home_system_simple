

class IntelligenceUnit:
    """
    An abstract class describing an intelligence unit
    """

    _inputs = None
    _outputs = None

    def __init__(self):
        pass

    def feed_inputs(self, inputs):
        """
        Feeds the input into the AI component
        :param inputs:
        :return:
        """
        self._inputs = inputs

    def think(self):
        """
        This method should be called when the AI works on inputs to produces its outputs,
        for instance finding outlying values.
        :return:
        """
        pass