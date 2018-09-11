from enum import Enum


class LogicOperators(Enum):
    OR = 0
    AND = 1
    NOT = 2
    IMPLIES = 3


class Formula:
    """
    Descibes a logical formula.
    """
    left = None
    right = None
    operator = None


    def __init__(self,*args):
        """

        """
        if len(args) < 2 or len(args) > 3:
            print("Not enough  or too many arguments (should give at least one operator and one formula")
            raise AttributeError()
        elif len(args)==2:
            self.right = args[1]
            self.operator = args[0]
        else:
            self.left = args[0]
            self.operator = args[1]
            self.right = args[2]

    def value(self):
        """
        Compute the truth value of the formula, given the values of the predicates.
        """
        if self.operator == LogicOperators.AND:
            try:
                return self.right.value() and self.left.value()
            except AttributeError as e:
                print(e.args)
        elif self.operator == LogicOperators.OR:
            try:
                return self.right.value() or self.left.value()
            except AttributeError as e:
                print(e.args)
        elif self.operator == LogicOperators.NOT:
            return not self.right.value()
        elif self.operator == LogicOperators.IMPLIES:
            return self.right.value() and (not self.left.value())


class Predicate(Formula):
    """
    This class describes a predicate, the basis of a logical formula
    """
    def __init__(self):
        pass

    def value(self):
        """
        Returns the valuation of the predicate, a boolean.
        """

class Rule(Formula):

    def __init__(self, *args):
            super().__init__(*args)

class Theory():
    """
    A theory is defined as a collection of rules
    """
    set_of_rules = None

    def __init__(self, *args, **kwargs):
        self.set_of_rules = []
        if len(args) > 0:
            for rule in args[0]:
                self.add_rule(rule)

    def add_rule(self,rule):
        if isinstance(rule,Rule):
            self.set_of_rules.append(rule)

