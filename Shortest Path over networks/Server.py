#Adrian Alex Jacobs
#3850269

from collections import defaultdict
import heapq
import socket
import sys
s=  socket.socket()
print("server created")

s.bind(('localhost',9999))

s.listen(3)
print("waiting for connections")

#Graph
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def build_graph(edge_list):
    graph = defaultdict(list)
    seen_edges = defaultdict(int)
    for src, dst, weight in edge_list:
        seen_edges[(src, dst, weight)] += 1
        if seen_edges[(src, dst, weight)] > 1:  # checking for duplicated edge entries
            continue
        graph[src].append((dst, weight))
        graph[dst].append((src, weight))  # remove this line of edge list is directed
    return graph

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Djikstra
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def dijkstra(graph, src, dst=None):
    nodes = []
    for n in graph:
        nodes.append(n)
        nodes += [x[0] for x in graph[n]]

    q = set(nodes)
    nodes = list(q)
    dist = dict()
    prev = dict()
    for n in nodes:
        dist[n] = float('inf')
        prev[n] = None

    dist[src] = 0

    while q:
        u = min(q, key=dist.get)
        q.remove(u)

        if dst is not None and u == dst:
            return dist[dst], prev

        for v, w in graph.get(u, ()):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev

def find_path(pr, node):  # generate path list based on parent points 'prev'
    p = []
    while node is not None:
        p.append(node)
        node = pr[node]
    return p[::-1]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Bellman Ford
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#MAIN()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    c, addr = s.accept()
    print("Client connected with", addr)
    
    c.send(bytes("Welcome to Server","utf-8"))
    
    
    #start , end, weight
    edges = [
        ("Bellville", "Nyanga", 0.80),
        ("Bellville", "SAPS",0.87 ),
        ("Bellville", "Bellville South", 0.48),
        ("Bellville", "Philippi", 0.67),
        ("Bellville", "Matland",  0.931),
        ("Bellville", "Parow", 1.54),
        ("Bellville", "Landsdowne", 0.88),
        ("Bellville", "Rondebosch", 0.93),
        ("Bellville", "Kuilsriver",  3),
        ("Bellville", "Sea Point",  0.84),
        ("Bellville", "Bishop Lavis",  0.7),
        ("Bellville", "Cape Town Central", 4),
        ("Bellville", "Table Bay Harbour",  0.94),
        ("Bellville", "Delft",  0.60),
        ("Bellville", "Mowbray",  4.8),
        ("Bellville", "Ravensmead",  0.65),
        ("Bellville", "Goodwood",  0.54),
        ("Bellville", "Elsies River",  4.86),
        ("Bellville", "Port of Entry",  1.095),
        ("Bellville", "Kensington",  0.55),
        ("Bellville", "Athlone",  0.74),
        ("Bellville", "Woodstock", 1.11),
        ("Bellville", "Pinelands",  1.168),
        ("Bellville", "Belhar",  2.53),
        ("Bellville", "Manenberg",  0.69),
        ("Bellville", "Claremont",  1.064),
    
    
        #didnt have time to code all the routes but here are my test routes that i used
        ("SAPS", "Matland",  0.6),
        ("Bellville South", "Woodstock", 3),
        ("Athlone", "Pinelands",  0.6),
        ("Goodwood", "Belhar", 0.78 ),
        ("Bellville", "Manenberg",  0.69),
        ("Manenberg", "Claremont",  1.3),
        ("SAPS", "Matland",  0.6),
        ("Bellville South", "Woodstock", 3),
        ("Athlone", "Pinelands",  0.6),
        ("Goodwood", "Belhar", 0.78 ),
        ("Bellville", "Manenberg",  0.69),
        ("Manenberg", "Claremont",  1.3),
        
        ("Elsies River", "Manenberg",  0.4),
        ("Sea Point", "Claremont",  4),
        ("SAPS", "Cape Town Central",  1.2),
        ("Belhar", "Woodstock", 0.94),
        ("Landsdowne", "Pinelands",  0.6),
        ("Rondebosch", "Belhar",1.5 ),
        ("Athlone", "Belhar",0.4 ),
    
    
    ]
    g = build_graph(edges)

    print("This is the graph")
    print(edges)
   


#Djikstra
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    src = c.recv(1024).decode()
    des = c.recv(1024).decode()
    
    print("\n=== Dijkstra ===")
    print("--- Single source, single destination ---")
    d, prev = dijkstra(g, src,des)
    path = find_path(prev, des)
    FINALPATH = "start at {} -> end at {}: weight = {}, path = {}".format(src,des,d, path)
    
    c.send(bytes(FINALPATH,"utf-8"))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------