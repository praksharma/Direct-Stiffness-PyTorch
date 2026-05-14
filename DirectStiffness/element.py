class Element():
    """
    MI is mass moment of inertia of the cross section.
    Cross_Area is cross section area of the element.
    Elastic_M is modulus of Elasticity.
    TODO: In future we might instead ask the user to input the breadth and depth of the element.
    """
    def __init__(self, id, Elastic_M, MI, Cross_Area, nodes) -> None:
        self.id = id
        self.Elastic_M = Elastic_M
        self.MI = MI
        self.Cross_Area =Cross_Area
        self.nodes = nodes
    def __str__(self):
        """A string returned when printing the object."""
        return f"Elem ID: {self.id}"
    def __repr__(self):
        "Give more information about the object for development purpose."
        return f"Elem ID: {self.id} Node IDs: [{self.nodes[0].id},{self.nodes[1].id}]"
