# Written By: Justin Pensock

# Solution to the quesiton on:
#       https://projecteuler.net/problem=18

"""
Maximum path sum (Based on Dijkstra's Algorithm)
        Arguments:
                graph -- adjacency list of a directed pyramid graph, with children mapped to their parent nodes
                node_weight -- mapping of each node to its weight
                source -- the source node (where the algorithm is referencing from)
                rows -- the number of rows in the pyramid graph
        Returns:
                The path from the top of the pyramid graph to one of the leaves that has the maximum aggregate sum across the nodes the path traverses
"""
def maxPathSum(graph, node_weight, source, rows):
        distances = {}
        path_sum = {}
        parents = {}
        p = {}

        # Building parents
        for node in graph.iterkeys():
                p[node] = []
                for par in graph.iterkeys():
                        if node in graph[par]:
                                p[node].append(par)

        # Initializing path sums to 0 for every node, except the leaves
        for v in graph.iterkeys():
                if (len(graph[v]) != 0):
                        path_sum[v] = 0
                else:
                        path_sum[v] = node_weight[v]

        # Q is a dictionary mapping rows to the nodes in that row
        Q = {}
        for r in range(rows):
                Q[r] = []
        i = 0
        j = 0
        for node in graph.iterkeys():
                Q[i].append(node)
                # Each n'th row has n entries
                if (i == j):
                        i += 1
                        j = 0
                else:
                        j += 1

        # The path search begins at the bottom row
        i = rows-1

        # Increment through the rows one at a time, updating the maximum path through each node
        #       in the row above it as we go
        while (i > 0):
                # Exhausted this row, move to the next one
                if (len(Q[i]) == 0):
                        i -= 1
                # Find the node with the largest path_sum from the source
                max_path = 0
                for node in Q[i]:
                        if (path_sum[node] > max_path):
                                max_path = path_sum[node]
                                u = node

                # Pop that node from the set if we've exhausted all of its parents
                Q[i].remove(u)
                # Search the path sums of each neighbor (to find a possible maximum path)
                for v in p[u]:
                        alt = path_sum[u] + node_weight[v]
                        # Longer path found, update the path_sum and parent of that node
                        if (alt >= path_sum[v]):
                                path_sum[v] = alt
                                parents[v] = u

        # Find the path taken to get the maximum sum (it begins at the source node)
        n = source
        opt_path = [source]
        while (len(graph[n]) != 0):
                n = parents[n]
                opt_path.append(n)

        # Print out the maximum path and its sum (in a pretty way)
        print "Maximum path:",
        for node in opt_path:
                if (len(graph[node]) != 0):
                        print str(node_weight[node]) + ' ->',
                else:
                        print str(node_weight[node])

        print "Maximum path sum: " + str(path_sum[source])
        

"""
Generates a directed triangle graph from the top-down
Creates an adjacency list, as a mapping of nodes to their neighbors
"""
def genTriangleGraph(rows):
        graph = {}
        x = -1
        y = 0
        # Generate a row
        for i in range(1, rows+1):
                if (i>=3):
                        y += 1
                        x += y
                # Generate each node in that row
                for j in range(i):
                        graph[i+j+x] = []
                        # Each node has 2 edges going to the two nodes underneath it (if they're there)
                        if (i != rows):
                                graph[i+j+x].append(2*i+j+x)
                                graph[i+j+x].append(2*i+j+x+1)
        return graph

def main():
        rows = 15
        # Generate the shell of the pyramid graph, where each node is labeled as an integer 0...n*(n-1)/2-1
        graph = genTriangleGraph(rows)

        # Weights for each of the nodes, as per the question describes
        graph_weights = {0:75,
                1:95, 2:64,
                3:17,4:47,5:82,
                6:18,7:35,8:87,9:10,
                10:20,11:4,12:82,13:47,14:65,
                15:19,16:1,17:23,18:75,19:3,20:34,
                21:88,22:2,23:77,24:73,25:7,26:63,27:67,
                28:99,29:65,30:4,31:28,32:6,33:16, 34:70, 35:92,
                36:41,37:41,38:26,39:56,40:83,41:40, 42:80, 43:70, 44:33,
                45:41,46:48,47:72,48:33,49:47,50:32, 51:37, 52:16, 53:94, 54:29,
                55:53,56:71,57:44,58:65,59:25,60:43, 61:91, 62:52, 63:97,64:51,65:14,
                66:70,67:11,68:33,69:28,70:77,71:73, 72:17, 73:78, 74:39,75:68,76:17,77:57,
                78:91,79:71,80:52,81:38,82:17,83:14, 84:91, 85:43, 86:58, 87:50, 88:27, 89:29, 90:48,
                91:63,92:66,93:4,94:68,95:89,96:53, 97:67, 98:30, 99:73,100:16,101:69,102:87,103:40,104:31,
                105:4,106:62,107:98,108:27,109:23,110:9, 111:70, 112:98, 113:73,114:93,115:38,116:53,117:60,118:4,119:23}

        maxPathSum(graph, graph_weights, 0, rows)

main()
