# Proposal for the CS 2.2 graph project.

## Description
The project idea that I had in mind was creating a graph out of something all Make School students
are familiar with, NPM! More specifically, I want to create a graph and tree out of the dependencies
inside of the node modules folder.

## Project model
Inside the npm graph, each package would be a vertex and the edges between vertices would serve as
what packages the current package depends on.

## Problems I would like to solve:
1. Figuring out which package is depended on the most through whichever vertex has the highest amount
of neighbors.
2. Proving that dependency graphs are acyclic, meaning that there are no cliques which would create
circular dependency issues.
3. Finding out the diameter of the top level package to the absolute bottom most package(s) (packages that
have no dependencies) to find the longest dependency chain/ longest load time for packages.
3. Creating a general tool that would allow for anyone to run my script and create a graph out
of their node projects node modules!

The structure of the node modules directory lends itself towards becoming a graph, making obtaining the
data to build the graph rather easy. Here is an example structure:

```
topLevel/
    - package.json
    - index.js
    - node_modules/
        - anotherPackage
            - package.json
            - index.js
            - node_modules
                - anotherPackage
                - ...
            - ...
        - anotherPackage
            - package.json
            - index.js
            - node_modules
```

As you can see, the structure of the folders are actually already structured *like a tree*, making
the traversal and information gathering very consistent across any node project.

