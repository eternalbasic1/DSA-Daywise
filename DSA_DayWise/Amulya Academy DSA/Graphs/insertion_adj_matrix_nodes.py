nodes = []
graph = []
node_count = 0

def add_node(v):
    global node_count
    if v in nodes:
        print(v," is already present in the graph")
        print()
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=' ')
        print()


print("before adding nodes")
print(nodes)
#print(graph)
print_graph()
print()
add_node("A")
add_node("B")
add_node("D")
add_node("E")
add_node("F")
print("After adding nodes")
print(nodes)
#print(graph)
print_graph()