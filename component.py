class Component:

    _id = -1
    _children = None
    _parents = None



    def __init__(self, *args, **kwargs):
        """
        :param args: id, TBD
            id |int| : the unique id number for this component
        :param kwargs: parents, children
            parents | dic<int,Component> | : dict of the parent components. Key is the id of the components
            children | dic<int,Component> | : dict of the child components. Key is the id of the components
        """
        if len(args) > 0:
            self._id = args[0]
        self._parents = kwargs.get("parents", {})
        self._children = kwargs.get("children", {})

    def get_id(self):
        return self._id
