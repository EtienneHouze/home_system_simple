from system import System
from component import Component
from can_module import CANModule

from copy import copy

class ControlSystem(System, CANModule):
    """
    A class to describe a system controlling a house, with a tree-like organization
    of sensors, controllers and other components.

    :Attributes:
        _components : a dict linking ids (int) to their components (Component) in the system
        _root : (Component) a pointer to the root component of the system
    """


    _components = {}
    _root = None


    def __init(self):
        super().__init__()
        self._components = {}

    def run(self):
        """
        Runs all the components in the system, from the root to the leaves of the components
        :return:
        """
        to_run = [self._root]
        next_run = []
        while len(to_run) > 0:
            for component in to_run:
                component.run()
                next_run.extend(component.get_children_list())
            to_run = copy(next_run)
            next_run = []

    def add_component(self, component, parents=None, children=None):
        """
        Adds a component to the system. Can also add parents and children to the component.
        :param component: the component to add
        :param parents: (list or singleton of int or Component) If specified, the parents to this component.
            The parents must already be in the system, and are represented by their id (int) or directly (Component)
        :return:
        """
        if component.get_id() in self._components.keys():
            print ("The id is not unique, check if the component is already in the system" +
                   " or change this component's id")
        else:
            self._components[component.get_id()] = component
            if parents is not None:
                if isinstance(parents, list):
                    for p in parents:
                        if isinstance(p,int):
                            if p in self._components.keys():
                                component.add_parent(self._components[p])
                            else:
                                print("The parent " + str(p) + " is not in this system")
                        elif isinstance(p, Component):
                            p_id = p.get_id()
                            if p_id in self._components.keys():
                                component.add_parent(p)
                            else:
                                print("The parent " + str(p_id) + " is not in this system")
                else:
                    p = parents
                    if isinstance(p, int):
                        if p in self._components.keys():
                            component.add_parent(self._components[p])
                        else:
                            print("The parent " + str(p) + " is not in this system")
                    elif isinstance(p, Component):
                        p_id = p.get_id()
                        if p_id in self._components.keys():
                            component.add_parent(p)
                        else:
                            print("The parent " + str(p_id) + " is not in this system")

    def get_root(self):
        """
        Finds the root of the control system (the root of the tree) and update the root attribute.
        Warns the user in case the root is not well-defined ( no root or multiple roots).
        :return: nothing
        """
        number_of_roots = 0
        for key in self._components.keys():
            if self._components[key].get_parents_number() == 0:
                number_of_roots += 1
                self._root = self._components[key]
        if number_of_roots > 1:
            print("Warning : Several roots exists, the system is not a Tree \n" +
                  "Running may cause unexpected results.")
        elif number_of_roots == 0:
            print("Warning : no root found, this system is not a tree \n"+
                  "Running is not possible")