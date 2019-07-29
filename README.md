# Proposal for the CS 2.2 graph project.

## Description
The project idea that I had in mind was creating a graph out of something all Make School students
are familiar with, NPM! More specifically, I want to create a graph and tree out of the dependencies
inside of the node modules folder that comes with every node project you create. This will allow for
all sorts of cool things like...

1. Creating a dependency tree to display the hierarchy of modules and then evaluating them.
2. Creating a dependency graph to show which modules rely on the same vertices (packages) and then
evaluating the resulting graph.
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

