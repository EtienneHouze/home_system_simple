from logic import Theory, Representation


class CANModule(Theory,Representation):
    """
    This class describes a module implementing the CAN thinking :
        - it can probe components with "spotlight" to find the cause of an anomaly
        - this module should be the only one in the system that can interact with the user
        to avoid a situation where every component tries to report activities to the user.
    """

    # TODO the can should work as follow : it should have a set of rules (a theory) and a set of predicates with valuations (the
    #  representation of the world), and then do the abduction operations to find which predicates are not correct in the
    # current representation, and report back.
    # The abduction should be done here, and not in the components.


    def __init__(self,*args,**kwargs):
        Theory.__init__(self,*args,**kwargs)
        Representation.__init__(self,*args,**kwargs)


    def solve_conflicts(self):
        """
        Solves the possible conflicts arising in the logical world.
        """
        main_conflict = None    # Pointer to the predicate with the most important conflict
        max_value = 0
        for pred in self._set_of_predicates:
            if (
                (pred.is_realized() and pred.get_value() < 0) 
                or ((not pred.is_realized()) and pred.get_value() > 0)
                ):
                if abs(pred.get_value()) > max_value:
                    main_conflict = pred
                    max_value = pred.get_value()
        if max_value is None:
            # do nothign if there is no conlict
            return
        while main_conflict is not None:
            # While we propagate the conflict to its possible causes
            for rule in self._set_of_rules:
                if main_conflict in rule.get_consequences():
                    possible_causes = rule.get_premises()
                    max_value = 0
                    for premise in rule.get_premises():
                        if ((premise.is_realized() and premise.get_value() < 0)
                            or ((not premise.is_realized()) and premise.get_value() > 0):
                            pass
