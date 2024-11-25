import heapq
class node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.huff = ""             # for huff code 

    def __lt__(self, next):
        return self.freq < next.freq


def print_nodes(node, val =""):

    new_val = val + str(node.huff)
    
    if(node.left):
        print_nodes(node.left, new_val)
    if(node.right):
        print_nodes(node.right, new_val)

    if(not node.left and not node.right):
        print(f"{node.freq} -> {new_val}")

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
nodes = []    # nodes to trace

for i in range(len(chars)):
    heapq.heappush(nodes, node(chars[i], freq[i]))


while len(nodes) > 1:
    left =  heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    newnode = node(left.char+right.char, left.freq+right.freq, left, right)
    heapq.heappush(nodes, newnode)


print_nodes(nodes[0])