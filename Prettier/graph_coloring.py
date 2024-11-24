adj_list = {
'A': ['B', 'D'],
'B': ['A', 'C'],
'C': ['B', 'D'],
'D': ['A' , 'C'],
}

colors = ['R', 'G']

class vertex:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
    
    def __eq__(self, value: object) -> bool:
        if self.color == value.color and self.name == value.name:
            return True
        return False
        
stack = []
starting_vertex = 'A'
vertexs = list(adj_list.keys())

for i in colors:
    
    stack.append(vertex(starting_vertex, i))
    expanded = {}
    i = 0

    while stack != []:
        
        current = stack.pop(-1)

        if i > vertexs.index(current.name):
            i = vertexs.index(current.name)

        neighbours = set(adj_list[current.name])
        expanded_vertex = set(expanded.keys())
        
        intersection = neighbours.intersection(expanded_vertex)

        if len(intersection) != 0:
            is_same_color_flag = False  
            for j in intersection:
                if expanded[j] == current.color:
                    is_same_color_flag = True
                    break
            
            if is_same_color_flag:
                continue

            expanded[current.name] = current.color
            i += 1

        else:
            expanded[current.name] = current.color
            i += 1

        #check sol
        if list(expanded.keys()) == vertexs:
            print(expanded)
            i -= 1
            to_remove = vertexs[i : ]
            for rem in to_remove:
                expanded.pop(rem, 0)
            i -= 1

        #expand:
        for color in colors:
            ver = vertex(vertexs[i], color)
            if ver not in stack and expanded.get(ver.name, -1) == -1:
                stack.append(ver)

        









