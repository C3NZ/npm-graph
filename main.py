import argparse
# Import the os module, for the os.walk function
import os

from graphs.digraph import Digraph
from graphs.graph import fill_graph
from graphs.utils.file_reader import read_graph_file
from graphs.vertex import Vertex


def traverse_npm_folder(root_path):
    seen_verts = set()
    vertices = [Vertex(root_path)]
    edges = []

    for dir_name, subdir_list, _ in os.walk("./" + root_path + "/node_modules/"):
        for subdir in subdir_list:
            if subdir not in seen_verts:
                vertices.append(Vertex(subdir))
                short_dir_name = os.path.basename(dir_name)
                edges.append(
                    (short_dir_name if short_dir_name else root_path, subdir, 1)
                )
                seen_verts.add(subdir)

    return vertices, edges


def process_args():
    """
        Process the arguments for the application
    """

    parser = argparse.ArgumentParser(
        description="Find the shortest path between two verticies"
    )
    parser.add_argument(
        "folder", help="The name of the npm based folder to parse", type=str
    )

    return parser.parse_args()


def main(args: argparse.Namespace):
    """
        Check if a path exists between two vertices.

        Args:
        * args - The parsed argument namespace from argparse
    """
    # Input checks
    if not args.folder:
        raise ValueError("There was no npm folder path specified!")

    vertices, edges = traverse_npm_folder(args.folder)
    graph = Digraph()
    # Obtain the graph properties and then fill out the graph.
    fill_graph(graph, vertices, edges)

    is_eulerian = graph.is_eulerian_cycle()
    print(f"This graph is Eulerian: {is_eulerian}")
    print(graph)


if __name__ == "__main__":
    ARGS = process_args()
    main(ARGS)
