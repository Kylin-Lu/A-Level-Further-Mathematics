# arcs = [4 , 5 , 5 , 6 , 6 , 7 , 8]
# nodes = ["DE" , "AE" , "BC" , "AD" , "BD" , "AB" , "CD"]
# num = 5
arcs = [8,8,10,10,11,12,12,13,14]
nodes = ["AD","BC","AC","CD","EF","CE","DE","DF","BE"]
num = 6

def Kruskal(arcs , nodes , num) :
    weight = arcs[0]
    node_list = [nodes[0]]
    nodes_list = []
    for i in range(1 , len(nodes) - 1) :
        first , last = nodes[i][0] , nodes[i][1]
        if len(nodes_list) < num :
            count = 0
        else :
            count = 1
        if len(node_list) > 1 :
            stop = False
            for a in range(1 , len(node_list)) :
                for b in range(0 , len(node_list[a])) :
                    if stop == False and node_list[a][b] in node_list[0] :
                        node_list[0] = node_list[0] + node_list[a]
                        node_list.pop(a)
                        stop = True
        if len(node_list) == 1 :
            length = len(node_list)
        else :
            length = len(node_list) - 1
        for x in range(0 , length) :
            if first in node_list[x] and last in node_list[x] and count == 0 :
                count = 1
            elif first not in node_list[x] and last not in node_list[x] and count == 0 :
                node_list.append(first + last)
                weight = weight + arcs[i]
                count = 1
                nodes_list.append(nodes[i])
            elif first not in node_list[x] and last in node_list[x] and count == 0 :
               node_list[x] = str(node_list[x] + first)
               weight = weight + arcs[i]
               count = 1
               nodes_list.append(nodes[i])
            elif first in node_list[x] and last not in node_list[x] and count == 0 :
                node_list[x] = str(node_list[x] + last)
                weight = weight + arcs[i]
                count = 1
                nodes_list.append(nodes[i])
    string = str("".join(set(node_list[0])))
    return string , weight

print(Kruskal(arcs , nodes , num))