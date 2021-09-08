


def RouteInspection() :
    (Vertex, Degree, Arc, Length) = ReadData()

    pass

def ReadData() :
    ReadDegree = open("DegreeList.txt" , "r")
    ReadLength = open("LengthList.txt" , "r")

    Vertex = []
    Degree = []
    Arc = []
    Length = []

    for line in ReadDegree.readlines() :
        line.strip("\n")
        Vertex.append(line[0])
        Degree.append(int(line[1:]))

    for line in ReadLength.readlines() :
        line.strip("\n")
        Arc.append(line[0 : 1])
        Length.append(int(line[2:]))

    return (Vertex , Degree , Arc , Length)

def Calculate(Arc , Length , Repeated) :
    TotalLength = sum(Length)

    for i in range(len(Repeated)) :
        Location = Arc.index(Repeated[i])
        TotalLength += Length[Location]

    return TotalLength