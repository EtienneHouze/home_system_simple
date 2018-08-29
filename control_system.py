from copy import copy


class ControlSystem:
    """
    Manages a collection of components, and makes sure each one has a different id
    """

    components = {}
    last_id = -1
    root = None

    def __init__(self):
        self.components = {}

    def find_root(self):
        for key in self.components.keys():
            if len(self.components[key]._parents) == 0:
                self.root = self.components[key]

    def run(self, in_system):
        self.root.in_goal[-3] = in_system
        to_run = [self.root]
        while len(to_run) > 0:
            new_run = []
            for component in to_run:
                for child_id in component._children.keys():
                    new_run.append(component._children[child_id])
                component.run()
            to_run = copy(new_run)