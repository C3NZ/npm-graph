import argparse
# Import the os module, for the os.walk function
import os

from graphs.graph import fill_graph
from graphs.utils.file_reader import read_graph_file

# Set the directory you want to start from
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

def traverse_npm_folder(root_path):


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

    traverse_npm_folder(args.folder)
    # Obtain the graph properties and then fill out the graph.
    graph, vertex, edges = read_graph_file(args.filename)
    fill_graph(graph, vertex, edges)

    is_eulerian = graph.is_eulerian_cycle()
    print(f"This graph is Eulerian: {is_eulerian}")


if __name__ == "__main__":
    ARGS = process_args()
    main(ARGS)
