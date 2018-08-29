class AISystem:

    _inputs = None
    _outputs = None

    def __init__(self):
        pass

    def feed_inputs(self,inputs):
        self._inputs = inputs

    def get_outputs(self):
        return self._outputs

    def think(self):
        pass

    def explain(self):
        """
        This method is called when the system is prompted to detect the origin of an anomaly.
        :return:

        """
        pass