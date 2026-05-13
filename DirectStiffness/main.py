
class Structure():
    """
    A class to denote the entire structure.
    Elems : List of elements
    """
    def read_file(self, input_file) -> None:
        pass

    def init_elems(self) -> None:
        pass

    def describe(self) -> None:
        "Describe the system based on the user input file. Tell user where is shear force, and what constrains are used. may be a diagram will be helpful."
        pass

    def check_constraints(self) -> None:
        "Check if only moments are passed or there exists a non-unique solution."
        pass
        
