from copy import copy


class Predicate:
    """
    A predicate, such as described in the CAN paper.
    A positive value denotes the predicate is either desired/believed true, and the amplitude of the value give the
    intensity of the desire/belief.
    """
    _value = 0
    _realisation = True

    def __init__(self, *args, **kwargs):
        """
        : param:
            args :

            kwargs :
                value : an int, the value of the desire
                realisation : a Boolean, whether the predicate is realised in the current state or not
        """
        self._value = kwargs.get("value",0)
        self._realisation = kwargs.get("realisation",True)

    def realize(self):
        self._realisation = True

    def contradict(self):
        self._realisation = False

    def is_realized(self):
        return self._realisation

    def get_value(self):
        return copy(self._value)

    def set_value(self, v):
        self._value = v


class Rule:

    def __init__(self, *args, **kwargs):
        pass


class Theory:

    _set_of_rules = None

    def __init__(self, *args, **kwargs):
        self._set_of_rules = []

    def add_rule(self, rule):
        if isinstance(rule,Rule):
            self._set_of_rules.append(rule)


class Representation:
    """
    A representation is a description of the world that is accessible to the 
    CAN module. It is a collection of predicates.
    """

    _set_of_predicates = None

    def __init__(self, *args, **kwargs):
        self._set_of_predicates = []

    def add_predicate(self, predicate):
        if isinstance(predicate, Predicate):
            self._set_of_predicates.append(predicate)

