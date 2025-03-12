import sys
from node import node, read_file
from scipy.cluster.hierarchy import DisjointSet

def MST_Prim(G, root):
    """
    Outputs a list of edges corresponding to an MST as calculated by Prim's algorithm
    To ensure consistent order, you're already given the root as the vertex with the lowest vertex name in lexicographic order
"""
    # do NOT change the lines below
    total_weight = 0
    root.key = 0
    root.parent = root
    import heapq
    heap = []
    T = []

    heapq.heappush(heap, root)

    # while heap is not empty, pop v from heap and check if it is already in the MST (using v.in_MST)
    while heap:
        v = heapq.heappop(heap)
        
        if v.in_MST:
            continue
        
        v.in_MST = True

    # Then, if it is not, add it to the MST, append it to T and add its v.key to total weights
            # We need to do this for every node not in the MST except the root, which is a special case
            # You can identify the root since for it, v.parent = v
            # For formatting consistency of the, append the edge to the root as a tuple (v,v.parent)
        total_weight += v.key

        if v.parent != v:
            T.append((v.name, v.parent.name))

    # Finally, iterate over negighbors u
            # for those whose edge cost is smaller than current key:
            # update their key to the edge weight
            # update their parent to v
            # add them to the heap
        for neighbor, weight in v.out_edges:
            if not neighbor.in_MST and weight < neighbor.key:
                neighbor.key = weight
                neighbor.parent = v
                heapq.heappush(heap, neighbor)

    return T, total_weight

def MST_Kruskal(G,E):
    # do NOT change the lines below

    total_weight = 0
    T = []

    disjoint_set = DisjointSet(G)

    # Sort the edges by weight, then iterate over them in order
    sorted_edges = sorted(E, key=lambda edge: edge[1])
    # For each edge, check if its two endpoints are already connected
    for (u, v), weight in sorted_edges:
    # If they are NOT connected, connect them, add them to the tree and their weight to the total
        if not disjoint_set.connected(u, v):
                disjoint_set.merge(u, v)
                T.append((u, v))
                total_weight += weight
    # Otherwise, ignore the edge

    return T, total_weight



def main():
    """
    Do NOT change main function
    Parses command-line arguments and runs the graph visualization.
    
    Usage:
    python script.py <filename> <algorithm>
    
    - <filename>: Path to the input file containing graph data.
    - <algorithm>: One of "PRIM", "KRUSKAL".

    """
    if len(sys.argv) < 3:
        print("Usage: python script.py <filename> <algorithm>")
        sys.exit(1)
    
    filename = sys.argv[1]
    algorithm = sys.argv[2].upper()
    allowed_algorithms = ["PRIM", "KRUSKAL"]
    
    if algorithm not in allowed_algorithms:
        print(f"Error: Invalid algorithm. Choose from {allowed_algorithms}")
        sys.exit(1)
    
    weighted = True  # Since we are building MST algorithms, we only care about weighted graphs
    directed = False # Let's ignore directed graphs for this assignment
    
    G, E = read_file(filename, weighted=weighted, directed=directed)
    # visualize_graph(G, weighted=weighted, directed=directed, layout="planar ")

    if algorithm == "PRIM":
        root = G[min(G.keys())]  # Do NOT change this line - the root should be the lowest node in lexicographical order for consistency
        MST, w = MST_Prim(G,root)
    if algorithm == "KRUSKAL":
        MST, w= MST_Kruskal(G,E)

    print(MST)
    print(w)


if __name__ == '__main__':
    main()
