OriginalArcs = []
OriginalLength = []
nodes = 0

def UseNearestNeighbor(OriginalArcs , OriginalLength , nodes) :
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
        print(StringWrite)