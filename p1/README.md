# AKIN KÜRŞAT ÖZKAN / 140709037

# Project 1: Search Algorithms in Action

Purpose of this project is that is creating implementation of Breadth-first, Depth-first and Uniform-cost searching algorithms in python.

The project works with grap input in txt format and chosen start and end states.

Sample input graph;

A:{A:0, B:6, C:3, D:4, E:0, F:0, G:0}

B:{A:6, B:0, C:2, D:0, E:4, F:0, G:0}

C:{A:3, B:2, C:0, D:2, E:0, F:8, G:0}

D:{A:4, B:0, C:2, D:0, E:3, F:0, G:0}

E:{A:0, B:4, C:0, D:3, E:0, F:7, G:6}

F:{A:0, B:0, C:8, D:0, E:7, F:0, G:6}

G:{A:0, B:0, C:0, D:0, E:6, F:6, G:0}

And the Implementation;

root@DESKTOP-TSJVH:/home/ceng3511/p1# python3 search.py graph.txt

Please enter the start state : A

Please enter the goal state : G

BFS : A - B - E - G

DFS : A - B - C - D - E - F - G

UCS : A - C - F - G

You can check python code from search.py file. In the file, there are also comments to explain every step of implementation


