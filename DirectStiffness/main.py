
class Structure():
    def __init__(self) -> None:
        print("Structure init called")

class Element():
    """
    I_M is mass moment of intertia of the cross section.
    A_M is cross section area of the element.
    E_M is modulus of Elasticity.
    TODO: In future we might instead askt he user to input the breadth and depth of the element.
    """
    def __init__(self, I_M=1*10^(-5), A_M=0.01, E_M=2*10^8) -> None:
        self.I_M = I_M
        self.A_M = A_M
        self.E_M = E_M