

class IntelligenceUnit:
    """
    An abstract class describing an intelligence unit
    In principle, the intelligence unit should be able to think, that means to describe the situation with
    words and to detect an out of ordinary situation.

    :Attributes:
        - _inputs : # TODO which data type ?
        - _ai_outputs : # The output should just be a boolean, posing if everything is nominal or not.
        - _description : a string produced by the AI component. It can be used by outer components to describe what
            is going on here.
    """
    # TODO : see how to deal with this class. For instance, what should be done here, only description of what
    # is happening, or also the abduction ?

    _inputs = None
    _ai_outputs = None
    _description = ""

    def __init__(self,*args,**kwargs):
        self._description = "Nothing to explain"

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
        This method should fill in both the _description and the _ai_outputs attributes.
        :return:
        """
        pass

    def get_description(self):
        """
        This method should be called by higher levels when they require an explanation for a
        malfunction
        :return:
        """
        return self._description