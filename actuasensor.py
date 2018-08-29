from component import Component
from system import System


class ActuaSensor(Component):

    system = None

    def __init__(self, **kwargs):
        parents = None
        children = None
        fun = None
        system = None
        id = -1
        if "parents" in kwargs.keys():
            parents = kwargs["parents"]
        else:
            parents = {}
        if "children" in kwargs.keys():
            children = kwargs["children"]
        else:
            children = {}
        if "id" in kwargs.keys():
            id = kwargs["id"]
        super().__init__(children=children,parents=parents,id=id)
        if "system" in kwargs.keys():
            system = kwargs.get("system")
        self.system = system
