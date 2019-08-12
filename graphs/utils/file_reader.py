"""
    Utils for all of the graph files
"""
from graphs.digraph import Digraph
from graphs.graph import Graph
from graphs.vertex import Vertex


def read_graph_file(filename: str) -> (Graph, [Vertex], [tuple]):
    """
        Read a graph file from the class specified format.

        Args:
        * filename - Read in the file specified by filename

        Returns:
            A tuple that contains a graph object and two lists
    """
    graph = Graph()
    verts = []
    edges = []
    is_weighted = None

    # Open up the file and parse the graph from text
    with open(filename, "r") as file:
        counter = 0

        # Iterate through the file
        for line in file:

            # Obtain the type of graph
            if counter == 0:
                graph_type = line.strip()
                if graph_type == "G":
                    graph = Graph()
                elif graph_type == "D":
                    graph = Digraph()
                else:
                    raise ValueError("Graph type not properly specified")

            # Obtain the verticies for the graph.
            elif counter == 1:
                for key in line.strip().split(","):
                    verts.append(Vertex(key))

            # Obtain all the edges.
            elif counter > 1:
                edge = line.strip("()\n").split(",")
                if is_weighted is None:
                    is_weighted = bool(len(edge) == 3)
                elif is_weighted and len(edge) < 3:
                    raise ValueError(
                        "You specified an edge with weights and one without. You should only do one or the other."
                    )

                if len(edge) != 3 and len(edge) != 2:
                    raise ValueError(
                        f"You specified an incorrect amount of args for the edge: {line}"
                    )
                edges.append(edge)
            counter += 1

    return graph, verts, edges
