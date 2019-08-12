"""
    Module that handles the Vertex objects to be inserted into any graph type.
"""


class Vertex:
    """
        The vertex object that is to be stored within a graph object

        Properties:
        * key - The key or label of the vertex.
    """

    def __init__(self, key: str):
        self.key = key
        self.__neighbors: list = []

    def __eq__(self, other_vert):
        return self.key == other_vert.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def __in_neighbors(self, vert):
        """
            Check if the vertex is already a neighbor to this current one

            Args:
            * vert - The other vertex object we're checking

            Returns:
            * True if the vert is found, false if not.

        """
        if not self.__neighbors:
            return False

        # Iterate through the graph
        for stored_vert, _ in self.__neighbors:
            if vert == stored_vert:
                return True

        return False

    @property
    def neighbors(self):
        """
            Function for getting the keys of the neighbors of the vertex

            Returns:
                A list of all neighbors to the current vertex
        """
        return self.__neighbors

    def add_neighbor(self, edge: tuple):
        """
            Function for adding a neighbor to this vertex

            Args:
            * edge - A tuple containing the vertex object and it's
            corresponding weight

            Returns:
            * True if the edge was successfully added, False if not.
        """
        vert, weight = edge
        if not self.__in_neighbors(vert):
            self.__neighbors.append((vert, float(weight)))
            return True
        return False
