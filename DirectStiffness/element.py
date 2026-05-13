class Element():
    """
    MI is mass moment of inertia of the cross section.
    Cross_Area is cross section area of the element.
    Elastic_M is modulus of Elasticity.
    TODO: In future we might instead askt he user to input the breadth and depth of the element.
    """
    def __init__(self, ID, Elastic_M, MI, Cross_Area, nodes) -> None:
        self.ID = ID
        self.Elastic_M = Elastic_M
        self.MI = MI
        self.Cross_Area =Cross_Area
        self.nodes = nodes
