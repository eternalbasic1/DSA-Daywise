#TODO : UNDIRECTED AND UNWEIGHTED GRAPH
'''
THIS IS FOR THE UNDIRECTED AND UNWEIGHTED GRAPH
'''


# nodes = []
# graph = []
# node_count = 0
#
# def add_node(v):
#     global node_count
#     if v in nodes:
#         print(v," is already present in the graph")
#         print()
#     else:
#         node_count += 1
#         nodes.append(v)
#         for n in graph:
#             n.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(graph[i][j],end=' ')
#         print()
#
# def add_edge(v1,v2):
#     if v1 not in nodes:
#         print(v1,"is not present in the graph")
#     elif v2 not in nodes:
#         print(v2, "is not present in the graph")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = graph[index2][index1] = 1
#
#
#
# print("before adding nodes")
# print(nodes)
# #print(graph)
# print_graph()
# print()
# add_node("A")
# add_node("B")
# add_node("D")
# add_edge('A','B')
# add_edge('A','D')
# print("After adding nodes")
# print(nodes)
# #print(graph)
# print_graph()



#TODO : UNDIRECTED AND WEIGHTED GRAPH
'''
THIS IS FOR THE UNDIRECTED AND WEIGHTED GRAPH
'''


# nodes = []
# graph = []
# node_count = 0
#
# def add_node(v):
#     global node_count
#     if v in nodes:
#         print(v," is already present in the graph")
#         print()
#     else:
#         node_count += 1
#         nodes.append(v)
#         for n in graph:
#             n.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(format(graph[i][j],"<3"),end=' ')
#         print()
#
# def add_edge(v1,v2,cost):
#     if v1 not in nodes:
#         print(v1,"is not present in the graph")
#     elif v2 not in nodes:
#         print(v2, "is not present in the graph")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = graph[index2][index1] = cost
#
#
#
# print("before adding nodes")
# print(nodes)
# #print(graph)
# print_graph()
# print()
# add_node("A")
# add_node("B")
# add_node("D")
# add_edge('A','B',10)
# add_edge('A','D',5)
# print("After adding nodes")
# print(nodes)
# #print(graph)
# print_graph()




#TODO : DIRECTED AND WEIGHTED GRAPH
'''
THIS IS FOR THE DIRECTED AND WEIGHTED GRAPH
'''


# nodes = []
# graph = []
# node_count = 0
#
# def add_node(v):
#     global node_count
#     if v in nodes:
#         print(v," is already present in the graph")
#         print()
#     else:
#         node_count += 1
#         nodes.append(v)
#         for n in graph:
#             n.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(format(graph[i][j],"<3"),end=' ')
#         print()
#
# def add_edge(v1,v2,cost):
#     if v1 not in nodes:
#         print(v1,"is not present in the graph")
#     elif v2 not in nodes:
#         print(v2, "is not present in the graph")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = cost
#
#
#
#
# print("before adding nodes")
# print(nodes)
# #print(graph)
# print_graph()
# print()
# add_node("A")
# add_node("B")
# add_node("D")
# add_edge('A','B',10)
# add_edge('A','D',5)
# print("After adding nodes")
# print(nodes)
# #print(graph)
# print_graph()



#TODO : DIRECTED AND UNWEIGHTED GRAPH
'''
THIS IS FOR THE UNDIRECTED AND WEIGHTED GRAPH
'''


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
            print(format(graph[i][j],"<3"),end=' ')
        print()

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1




print("before adding nodes")
print(nodes)
#print(graph)
print_graph()
print()
add_node("A")
add_node("B")
add_node("D")
add_edge('A','B')
add_edge('A','D')
print("After adding nodes")
print(nodes)
#print(graph)
print_graph()