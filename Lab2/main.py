import heapq
def dijkstraMinHeap(adjList, start=0):
    V = len(adjList)  # Number of vertices
    S = [False] * V  # Visited set
    d = [float('inf')] * V  # Distance array
    pi = [-1] * V  # Previous node array
    d[start] = 0
    pq = [(0, start)]  # Min heap priority queue
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if S[current_node]:
            continue
        S[current_node] = True
        
        for neighbor, weight in adjList[current_node]:
            if not S[neighbor]:
                new_dist = current_dist + weight
                if new_dist < d[neighbor]:
                    d[neighbor] = new_dist
                    pi[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return d, pi

def dijkstraArray(adjMatrix):
    V = len(adjMatrix)
    d = [float('inf')] * V
    pi = [-1] * V
    d[0] = 0  # Distance to source is 0
    S = [False] * V  # Visited array 
    for _ in range(V):
        # Find the unvisited node with the smallest known distance
        min_distance = float('inf')
        nextNode = -1
        for v in range(V):
            if not S[v] and d[v] < min_distance:
                min_distance = d[v]
                nextNode = v
        if nextNode == -1:
            break  # All remaining nodes are unreachable
        S[nextNode] = True  # Mark node as visited

        for neighbor in range(V):
            weight = adjMatrix[nextNode][neighbor]
            if weight > 0 and not S[neighbor]:  # Ignore 0-weight (no direct edge)
                new_distance = d[nextNode] + weight
                if new_distance < d[neighbor]:
                    d[neighbor] = new_distance
                    pi[neighbor] = nextNode

    return d, pi

