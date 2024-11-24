import numpy as np

def bellman_ford(nodes, edges, source_index = 0):
    path_len = {v: float('inf') for v in nodes}
    path_len[source_index] = 0

    path = {v : [] for v in nodes}
    path[source_index] = [source_index]

    for _ in range(len(nodes) - 1):
        for(u,v) , w_uv in edges.items():
            if path_len[u] + w_uv < path_len[v]:
                path_len[v] =path_len[u] + w_uv
                path[v] = path[u] + [v]
    
    for (u,v), w_uv in edges.items():
        if path_len[u] + w_uv < path_len[v]:
            print('Graph has a negative cycle')

    return path_len, path


nodes = [0 ,1 , 2, 3]

edges = {
    (0 , 1) : 1.0,
    (1 , 0) : 1.0,
    (0, 2) : 1.5,
    (2, 0) : 1.5,
    (0, 3) : 2.0,
    (3, 0) : 2.0,

    (1 , 3) : 0.5,
    (3 , 1) : 0.5,
    
    (2 , 3) : 1.5,
    (3 , 2) : 1.5,
}

path_len , paths = bellman_ford(nodes, edges)

print(path_len)
print(paths)


