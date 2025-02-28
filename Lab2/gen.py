import random 

def gen_connected_graph(n:int, m:int) -> list:

    graph = []
    for i in range(1,n):
        graph.append([i-1,i])
    while(len(graph) < m): 
        a = random.randint(1,n)
        b = random.randint(1,n)
        a -= 1
        b -= 1
        if(a > b): 
            temp = a
            a = b
            b = temp
        if(a == b or [a,b] in graph): continue
        graph.append([a,b])

    weighted_graph = []
    for i in graph:
        temp = i.copy()
        weight = random.randint(1,5000)
        temp.append(weight)
        weighted_graph.append(temp)
    return graph,weighted_graph

def adj_list(n:int,g:list) -> list:
    adj = [[] for _ in range(n+1)]
    for edge in g: 
        u = edge[0]
        v = edge[1]
        w = edge[2]
        adj[u].append([v,w])
        adj[v].append([u,w])
    return adj

def adj_matrix(n:int,g:list) -> list:
    adj = [[0 for i in range(n+1)] for j in range(n+1)]
    for edge in g: 
        u = edge[0]
        v = edge[1]
        w = edge[2]
        adj[u][v] = w
        adj[v][u] = w
    return adj

def gen_completed_graph(n:int) -> list:
    graph = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            graph.append([i,j])
    weighted_graph = []
    for g in graph:
        w = random.randint(1,5000)
        weighted_graph.append([g[0]-1,g[1]-1,w])
    return graph, weighted_graph