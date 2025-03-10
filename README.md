# 349lab3

For this assignment, you will implement the two algorithms for calculating a Minimum Spanning Tree seen in class: Prim's and Kruskal's

A spanning tree of a connected weighted graph G= {V,E} is a set of edges T such that:

T is a subset of E
The graph {V,T} is a tree
Remember that we defined tree as an acyclic, connected graph
A minimum spanning tree (MST) is a spanning tree whose total weight (the sum of weights of edges in T) is minimum (no other spanning tree has smaller weight)

For this assignment, you may assume that G a connected, undirected, weighted graphs with at least two vertices and one edge

Sample materials
I am providing you with three python files:

A file node.py Download node.pycontaining a node class and a method to read a graph from a file
A file visualize_graph.py Download visualize_graph.pycontaining a method to visualize a given graph
This file is optional but could help you visualize a graph that you built as a test case 
If a particular graph looks messy with multiples overlaps or intersections, try changing the layout from planar to one of the others provided in the layout functions dictionary
A prompt file MST_prompt.py Download MST_prompt.pycontaining code that reads a graph (from the method defined in node.py) and provides instructions for the two algorithms
I am also providing you with two sample input files: MST_slides_example Download MST_slides_example (seen in the slides) and MST_prompt.py Download MST_prompt.py(seen in exercise sheet)

You are encouraged to build your own test cases. The format for the input file is as follows:

The first line contains a number n, representing the number of vertices in the graph
The next n lines will contain the names of the vertices, one per line. Make sure each name is unique
After that, an arbitrary number of lines will represent and edge by two vertex names followed by the weight, all separated by commas
Remember that the graph will be read as undirected, and that your algorithm is not required to work for graphs with multiple connected components
    Usage:
    python script.py <filename> <algorithm>
    - <filename>: Path to the input file containing graph data.
    - <algorithm>: One of "PRIM", "KRUSKAL".

    Example outputs (see output formatting below)

Algorithms
You will implement  both Prim's and Kruskal's algorithms. The MST_prompt.py Download MST_prompt.pyhas detailed instructions for each, but you may also refer to the slides for the full pseudocode

For Prim, you will build a single spanning subtree one node at a time, by adding at each step the edge with smallest weight between a node in the tree and a node not on the tree. You will use a min heap to store nodes scheduled to be visited. Whenever you pop a node v not yet in the tree:

Set its v.in_MST attribute to True
Add an edge (v, v.parent) to T and its key value to the total weight unless v is the root. Be consistent with the order to standardize the output format.
Iterate over neighbors u, checking their current key
If the edge (v,u) weights less than the current value of u.key, push it to the heap and update u.key and u.parent. Ad
Return both the list of tree edges and the total weight
For Kruskal, you will keep a disjoint subsets of the graph   (starting with one vertex per set). Iterate over all edges in ascending weight order (you will need to sort) and then, 

Check if the edge (u,v) are already in the same subset using disjoint_set.connected. If they are, skip that edge.
Otherwise:
Merge u and v using disjoint_set.merge
Add (u,v) to T and its weight to the graph
Deliverable and output
Rename MST_prompt.py Download MST_prompt.pyto your_net_id_lab3.py and implement MST_Prim and MST_Kruskal. Do not upload more than one file or a zip file.

The main function already prints T and the total weight. Your submission should not modify main and should not print anything else.

Example outputs:

python rcanaan_lab3.py MST_slides_example prim

>> [('c', 'a'), ('e', 'c'), ('h', 'e'), ('i', 'h'), ('f', 'i'), ('g', 'f'), ('d', 'g'), ('b', 'e')]

>> 18

python rcanaan_lab3.py MST_slides_example kruskal

>> [('a', 'c'), ('d', 'g'), ('e', 'h'), ('f', 'g'), ('h', 'i'), ('f', 'i'), ('b', 'e'), ('c', 'e')]

>> 18

python rcanaan_lab3.py MST_slides_example prim  

>> [('f', 'a'), ('c', 'f'), ('k', 'a'), ('l', 'k'), ('e', 'c'), ('g', 'k'), ('b', 'e'), ('i', 'b'), ('j', 'i'), ('d', 'j'), ('h', 'g')]

>> 87

python rcanaan_lab3.py MST_slides_example kruskal

>> [('b', 'e'), ('a', 'f'), ('k', 'l'), ('c', 'f'), ('i', 'j'), ('a', 'k'), ('b', 'i'), ('c', 'e'), ('d', 'j'), ('g', 'k'), ('g', 'h')]

>> 87
