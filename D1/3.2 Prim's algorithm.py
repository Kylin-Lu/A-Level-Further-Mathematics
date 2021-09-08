# arcs = [4 , 5 , 5 , 6 , 6 , 7 , 8]
# nodes = ["DE" , "AE" , "BC" , "AD" , "BD" , "AB" , "CD"]
# num = 5
arcs = [8,8,10,10,11,12,12,13,14]
nodes = ["AD","BC","AC","CD","EF","CE","DE","DF","BE"]
num = 6

def Bubble(list , arcs) :
    for x in range(1 , len(list)) :
        for i in range(0 , len(list) - x) :
            if list[i] > list[i + 1] :
                list[i] , list[i + 1] = list[i + 1] , list[i]
                arcs[i] , arcs[i + 1] = arcs[i + 1] , arcs[i]
    return list , arcs

(arcs , nodes) = Bubble(arcs , nodes)

def Prim(arcs , nodes , num) :
    selected = []
    joined = ""
    length = 0
    all = ""

    if len(arcs) != len(nodes) :
        return "Error . Please check the list ."

    for i in range(len(nodes)) :
        all += nodes[i]

    start = input("Please enter the vertex to start : ")

    while start not in all :
        start = input("The vertex does not exist . Please enter the vertex to start : ")

    for i in range(len(nodes)) :
        if start in nodes[i] :
            joined += nodes[i]
            selected.append(nodes[i])
            length += arcs[i]
            del nodes[i]
            del arcs[i]
            break

    while len(joined) != num :
        for i in range(len(nodes)):
            if nodes[i][0] in joined and nodes[i][1] in joined:
                pass
            elif nodes[i][0] in joined or nodes[i][1] in joined:
                selected.append(nodes[i])
                length += arcs[i]
                if nodes[i][0] in joined:
                    joined += nodes[i][1]
                else:
                    joined += nodes[i][0]
                del nodes[i]
                del arcs[i]
                break

    return selected , length

print(Prim(arcs , nodes , num))