"""
    Module that implements a directed graph class through the extension of the
    undirected graph class (from challenges.graphs.graph)
"""
from graphs.graph import Graph


class Digraph(Graph):
    """
        Class for representing a directed graph

        Inherits properties and functions from the Graph class
    """

    def __repr__(self):
        return f"<Digraph> - {self.verticies} verts - {self.edges} edges"

    def add_edge(self, from_vert: str, to_vert: str, weight: float = 1.0):
        """
           Function for adding an edge to the digraph

           Args:
           * fromVert - The vertex object we're connecting the toVert to
           * toVert - The vertex object we're connecting the fromVert to
           * weight - (1.0) - The weight of the edge
        """

        # Error handling before trying to add an edge
        if from_vert not in self.graph or to_vert not in self.graph:
            print(from_vert in self.graph)
            print(to_vert)

            raise ValueError("One of the verticies is not currently in the graph.")
        if from_vert == to_vert:
            raise ValueError("You cannot have a vertex connect to itself.")

        # The from and to vertex objects within our graph
        from_vert_obj = self.graph[from_vert]
        to_vert_obj = self.graph[to_vert]

        # Add the neighbors to the vertex
        added_from = from_vert_obj.add_neighbor((to_vert_obj, weight))
        if added_from:
            self.edges += 1

    def get_edges(self) -> [tuple]:
        """
            Function for getting all of the edges from the graph

            Returns:
            * A list of the unique edges within the graph.
        """
        unique_edges: set = set()

        # Iterate through all of the edges within the graph
        for vert_key, vert in self.graph.items():

            # Iterate through all of the neighbors of the current vertex
            for neighbor_vert, weight in vert.neighbors:
                edge = (vert.key, neighbor_vert.key, int(weight))
                unique_edges.add(edge)

        return list(unique_edges)
