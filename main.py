import argparse
# Import the os module, for the os.walk function
import os

from graphs.digraph import Digraph
from graphs.graph import fill_graph
from graphs.utils.file_reader import read_graph_file
from graphs.vertex import Vertex


def traverse_npm_folder(root_path):
    seen_verts = set()
    edges = []
    real_root = root_path.split("/")[-1]
    vertices = {real_root: Vertex(real_root)}

    for dir_name, subdir_list, _ in os.walk("./" + root_path + "/node_modules"):
        pkg, node_module = dir_name.split("/")[-2], dir_name.split("/")[-1]
        for subdir in subdir_list:
            if node_module == "node_modules" and subdir != ".bin":
                vertices[subdir] = Vertex(subdir)
                short_dir_name = os.path.basename(pkg)

                if short_dir_name == "":
                    short_dir_name = real_root

                if short_dir_name in vertices and short_dir_name != subdir:
                    edges.append((subdir, short_dir_name, 1))

    return vertices.values(), edges


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

    vertices, edges = traverse_npm_folder(args.folder.rstrip("/"))
    graph = Digraph()
    # Obtain the graph properties and then fill out the graph.
    fill_graph(graph, vertices, edges)

    hist = dict()
    root = args.folder.rstrip("/").split("/")[-1]
    print("#### START EVALUATION ####\n")
    print(f"\tExamining the directory: {root}")
    highest = 0
    dependency = ""
    for key, vertex in graph.graph.items():
        if len(vertex.neighbors) > highest:
            highest = len(vertex.neighbors)
            dependency = key

    print(f"\tMost depended on package: {dependency} with {highest} dependants")
    path_len, package = graph.find_longest_path()
    print(
        f"\tThe longest shortest path was: {path_len} edges and to the package: {package}"
    )
    is_acyclic = graph.prove_acyclic(args.folder.strip("/").split("/")[-1])
    print(f"\tThe graph is acyclic: {is_acyclic}")
    print("\n#### END EVALUATION ####")


if __name__ == "__main__":
    ARGS = process_args()
    main(ARGS)
