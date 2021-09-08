'''
A program used to solve The Travelling Salesman problem .
Written By Kylin Lu . Start from Dec 4th 2020
Still developing , the RMST is finished .
'''

def MainProgram() :
    nodes= ""
    (OriginalArcs, OriginalLength) = Bubble()

    for i in range(len(OriginalArcs)) :
        first , second = OriginalArcs[i][0] , OriginalArcs[i][1]
        if first not in nodes and second not in nodes :
            nodes += first + second
        elif first not in nodes :
            nodes += first
        elif second not in nodes :
            nodes += second
        else :
            pass

    LowerBound = UseRMST(OriginalArcs , OriginalLength , nodes)
    UpperBound = UseNearestNeighbor(OriginalArcs , OriginalLength , nodes)

    print("The range is : " + str(LowerBound) + " < Optimal solution <= " + str(UpperBound))

def ReadFile() : # read the file
    File = open("ArcList.txt" , "r")
    OriginalArcs = []
    OriginalLength = []

    for line in File.readlines() :
        OriginalArcs.append(line.strip("\n")[0:2])
        OriginalLength.append(int(line.strip("\n").replace(line.strip("\n")[0:2] , "")))

    return (OriginalArcs , OriginalLength)

def Bubble() : # sort the list
    (arcs , length) = ReadFile()

    if len(arcs) != len(length) :
        print("Data out of range . Please recheck the 'ArcList.txt' file format .")
        exit()
    else :
        for x in range(1, len(arcs)):
            for i in range(0, len(arcs) - x):
                if length[i] > length[i + 1]:
                    length[i], length[i + 1] = length[i + 1], length[i]
                    arcs[i], arcs[i + 1] = arcs[i + 1], arcs[i]
                else :
                    pass

    return (arcs , length)

def UseRMST(OriginalArcs , OriginalLength , nodes) : # find the biggest lower bound
    LowerBound = 0
    Write = open("LowerBoundList.txt" , "w")

    for i in range(len(nodes)) : # Repeat delete one node
        StringWrite = ""

        ArcsUsing = []
        LengthUsing = []
        ArcsDeleted = []
        LengthDeleted = []

        UsedNodes = ""
        Length = 0
        UsedArcs = []
        AddArcs = []

        NodeDeleted = nodes[i]
        NodesUsing = nodes
        NodesUsing = NodesUsing.replace(NodeDeleted , "")

        StringWrite += "The node has been deleted is : " + NodeDeleted + "\n"

        for j in range(len(OriginalArcs)) : # Refresh the lists are using
            if NodeDeleted not in OriginalArcs[j] :
                ArcsUsing.append(OriginalArcs[j])
                LengthUsing.append(OriginalLength[j])
            else :
                ArcsDeleted.append(OriginalArcs[j])
                LengthDeleted.append(OriginalLength[j])

        while len(UsedNodes) != len(NodesUsing) : # Find the lower when delete that node
            Length += LengthUsing[0]
            UsedNodes += ArcsUsing[0]
            UsedArcs.append(ArcsUsing[0])

            for j in range(1, len(ArcsUsing)) : # find Reduce Minimum Spanning Tree
                First = ArcsUsing[j][0]
                Second = ArcsUsing[j][1]

                if First not in UsedNodes and Second not in UsedNodes :
                    Length += LengthUsing[j]
                    UsedNodes += First + Second
                    UsedArcs.append(ArcsUsing[j])
                elif First not in UsedNodes :
                    Length += LengthUsing[j]
                    UsedNodes += First
                    UsedArcs.append(ArcsUsing[j])
                elif Second not in UsedNodes :
                    Length += LengthUsing[j]
                    UsedNodes += Second
                    UsedArcs.append(ArcsUsing[j])
                else :
                    pass

                if len(UsedNodes) == len(NodesUsing) :
                    break

        StringWrite += "The RMST used : " + str(UsedArcs) + " . The weight of it is : " + str(Length) + "\n"

        for j in range(2) :
            Length += LengthDeleted[j]
            AddArcs.append(ArcsDeleted[j])

        StringWrite += "Then add : " + str(AddArcs) + " . The weight now is : " + str(Length) + "\n"

        Write.write(StringWrite)

        if LowerBound < Length :
            LowerBound = Length
        else :
            pass

    Write.close()
    return LowerBound

def UseNearestNeighbor(OriginalArcs , OriginalLength , nodes) :
    UpperBound = 999999999
    Write = open("UpperBoundList.txt", "w")

    for i in range(len(nodes)) : # Repeat with starting from different nodes
        Length = 0
        Start = nodes[i]
        StringWrite = "The starting point is : " + Start + "\n"

        ArcsUsing = []
        LengthUsing = []
        UsedArcs = []
        Next = Start

        for j in range(len(OriginalArcs)) : # New list for working
            ArcsUsing.append(OriginalArcs[j])
            LengthUsing.append(OriginalLength[j])

        while len(UsedArcs) != len(nodes) - 1 : # Use nearest neighbor
            j = 0
            Found = False

            while Found == False :
                First = ArcsUsing[j][0]
                Second = ArcsUsing[j][1]

                if Next == First :
                    Length += LengthUsing[j]
                    UsedArcs.append(ArcsUsing[j])
                    Next = Second

                    count = 0
                    while count != len(ArcsUsing) :
                        if First in ArcsUsing[count]:
                            del ArcsUsing[count]
                            del LengthUsing[count]
                        else :
                            count += 1

                    Found = True
                elif Next == Second :
                    Length += LengthUsing[j]
                    UsedArcs.append(ArcsUsing[j])
                    Next = First

                    count = 0
                    while count != len(ArcsUsing):
                        if Second in ArcsUsing[count]:
                            del ArcsUsing[count]
                            del LengthUsing[count]
                        else:
                            count += 1

                    Found = True
                else :
                    j += 1

        StringWrite += "The nearest neighbour used : " + str(UsedArcs) + " . The weight of it is : " + str(Length) + "\n"

        AddArc = Start + Next
        AddArc = "".join((lambda x: (x.sort(), x)[1])(list(AddArc)))
        LocationAddArc = OriginalArcs.index(AddArc)
        Length += OriginalLength[LocationAddArc]

        StringWrite += "Then add : " + str(AddArc) + " . The weight now is : " + str(Length) + "\n"

        Write.write(StringWrite)

        if Length < UpperBound :
            UpperBound = Length
        else :
            pass

    Write.close()
    return UpperBound

MainProgram()