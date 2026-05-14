
from .utils import Config
from .nodes import Node
from .element import Element
import torch

class Structure():
    """
    A class to denote the entire structure.
    Elems : List of elements
    """
    def __init__(self) -> None:
        self.cfg = Config()  # get the cfg details
    def read_file(self, input_file) -> None:
        "Some sort of json file input."
        pass

    def read_variables(self, variable) -> None:
        """
        Pass the input in a python dictionary instead of files. So something like the following.
        variable = {
                    "materials": {
                        "E": [2e8, 2e8],
                        "I": [4e-6, 4e-6],
                        "A": [0.0, 0.0],
                    },
                    "nodes": [
                        [0.0, 0.0],
                        [5.0, 0.0],
                        [10.0, 0.0],
                    ],
                    "connectivity": [
                        [0, 1],
                        [1, 2],
                    ],
                    "free_dofs": [4, 5],
                    "loads": {
                        4: -1.0,
                    },
                }
        """
        self.init_nodes(variable["nodes"])
        self.init_elems(variable["materials"], variable["connectivity"])

    def init_nodes(self, nodes) -> None:
        self.nodes = []
        for idx, node in enumerate(nodes):
            self.nodes.append(Node(idx, node[0], node[1])) # id, x, y
            print(self.nodes[idx])


    def init_elems(self, materials, connectivity) -> None:
        self.elems = []
        
        for idx, conn in enumerate(connectivity):
            self.elems.append(Element(idx,
                                      materials["E"][idx],
                                      materials["I"][idx],
                                      materials["A"][idx],
                                      [self.nodes[conn[0]], self.nodes[conn[1]]]
                                      )
                            ) # id, E, I, A, [node[0], node[1]]
            print(self.elems[idx])


    def describe(self) -> None:
        "Describe the system based on the user input file. Tell user where is shear force, and what constrains are used. may be a diagram will be helpful."
        pass

    def check_constraints(self) -> None:
        "Check if only moments are passed or there exists a non-unique solution."
        pass
        
