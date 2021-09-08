def Bubble(arcs , length) : # sort the list
    for x in range(1 , len(arcs)):
        for i in range(0 , len(arcs) - x):
            if length[i] > length[i + 1]:
                length[i] , length[i + 1] = length[i + 1] , length[i]
                arcs[i] , arcs[i + 1] = arcs[i + 1] , arcs[i]
            else :
                pass
    print(arcs , length)
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
                    for k in range(j , len(ArcsUsing)) :
                        x = ArcsUsing[k][0]
                        y = ArcsUsing[k][1]

                        if x in UsedNodes and (y == First or y == Second) :
                            Length += LengthUsing[k]
                            Length += LengthUsing[j]
                            UsedNodes += First + Second
                            UsedArcs.append(ArcsUsing[k])
                            UsedArcs.append(ArcsUsing[j])
                            break
                        elif y in UsedNodes and (x == First or x == Second) :
                            Length += LengthUsing[k]
                            Length += LengthUsing[j]
                            UsedNodes += First + Second
                            UsedArcs.append(ArcsUsing[k])
                            UsedArcs.append(ArcsUsing[j])
                            break
                            
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


########################################################################################################################
import wx
import wx.grid
import wx.xrc


class GetNumbOfVertex(wx.Frame) :
    def __init__(self , parent) :
        wx.Frame.__init__(self , parent , id = wx.ID_ANY , title = "Number of vertex" , pos = wx.DefaultPosition,
                              size = wx.Size(400 , 80) , style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints((400 , 80) , (400 , 80))

        MainSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.Text = wx.StaticText(self , wx.ID_ANY , u"Please select the number of vertex : " , wx.DefaultPosition , wx.DefaultSize , 0)

        Choices = ["3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "11" , "12" , "13" , "14" , "15" , "16"]
        self.Select = wx.Choice(self , wx.ID_ANY , wx.DefaultPosition , wx.DefaultSize , Choices)
        self.Select.SetSelection(0)

        self.Button = wx.Button(self , wx.ID_ANY , u"  Continue" , wx.DefaultPosition , wx.DefaultSize , 0)

        MainSizer.AddMany([(self.Text , 0 , wx.ALL , 12) , (self.Select , 0 , wx.UP , 8) , (10 , 0 , 0) , (self.Button , 0 , wx.UP , 8)])

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Button.Bind(wx.EVT_BUTTON , self.FinishChoice)

    def FinishChoice(self , event) :
        Numb = int(self.Select.GetSelection())
        Numb += 3
        Create = CreateGird(None , Numb)
        Create.Show()
        self.Destroy()


class CreateGird(wx.Frame) :
    def __init__(self , parent , NumbOfVertex) :

        wx.Frame.__init__(self , parent , id = wx.ID_ANY , title = "Least Distance Table" , pos = wx.DefaultPosition ,
                          size = wx.Size((NumbOfVertex + 2 ) * 40 , (NumbOfVertex + 3) * 40 + 16) ,
                          style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(((NumbOfVertex + 2 ) * 40 , (NumbOfVertex + 3) * 40 + 16) , ((NumbOfVertex + 2 ) * 40 , (NumbOfVertex + 3) * 40 + 16))

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.DistanceTable = wx.grid.Grid(self , wx.ID_ANY , wx.DefaultPosition , wx.DefaultSize , 0)

        ## Setup table
        self.DistanceTable.CreateGrid(NumbOfVertex , NumbOfVertex)
        self.DistanceTable.EnableEditing(True)
        self.DistanceTable.EnableGridLines(True)
        self.DistanceTable.EnableDragGridSize(False)
        self.DistanceTable.SetMargins(0, 0)
        self.DistanceTable.SetDefaultCellAlignment(wx.ALIGN_CENTER , wx.ALIGN_CENTER)

        ## Set column
        self.DistanceTable.EnableDragColMove(False)
        self.DistanceTable.EnableDragColSize(False)
        self.DistanceTable.SetColLabelSize(40)
        self.DistanceTable.SetColLabelAlignment(wx.ALIGN_CENTRE , wx.ALIGN_CENTRE)

        ## Set rows
        self.DistanceTable.EnableDragRowSize(False)
        self.DistanceTable.SetRowLabelSize(40)
        self.DistanceTable.SetRowLabelAlignment(wx.ALIGN_CENTRE , wx.ALIGN_CENTRE)

        ## Set values
        for i in range(NumbOfVertex) :
            self.DistanceTable.SetColSize(i , 40)
            self.DistanceTable.SetRowSize(i , 40)
            self.DistanceTable.SetColLabelValue(i , chr(65 + i))
            self.DistanceTable.SetRowLabelValue(i, chr(65 + i))

            self.DistanceTable.SetCellValue(i , i , "-")
            self.DistanceTable.SetReadOnly(i , i , True)

            for j in range(NumbOfVertex) :
                if i != j :
                    self.DistanceTable.SetCellValue(i , j , "0")
                    self.DistanceTable.SetCellEditor(i , j , wx.grid.GridCellNumberEditor())

        self.FinishButton = wx.Button(self , wx.ID_ANY , u"Finish" , wx.DefaultPosition , wx.DefaultSize)

        MainSizer.AddMany([(self.DistanceTable , 0 , wx.ALL , 10) , (self.FinishButton , 0 , wx.LEFT , (NumbOfVertex) * 18)])

        self.SetSizer(MainSizer)
        self.Layout()
        self.Centre(wx.BOTH)

        self.Numb = NumbOfVertex
        self.FinishButton.Bind(wx.EVT_BUTTON , self.ToCalculate)
        self.DistanceTable.Bind(wx.grid.EVT_GRID_CELL_CHANGED , self.SyncTable_GetLocation)


    def ToCalculate(self , event) :
        (StartArcs, StartLengths) = self.ReadData(None , self.Numb)

        if 0 in StartLengths :
            box = wx.MessageDialog(None, u"There should not have 0 in the least distance table", u"Error", wx.OK | wx.CENTRE)
            box.ShowModal()
            box.Destroy()
            return

        self.Answer = self.Calculate(None , StartArcs, StartLengths)

        box = wx.MessageDialog(None , self.Answer , u"Solution", wx.OK | wx.CENTRE)
        box.ShowModal()
        box.Destroy()


    def ReadData(self , parent , NumbOfVertex) :
        StartArcs = []
        StartLengths = []

        for i in range(NumbOfVertex) :
            Range = NumbOfVertex - i
            for j in range(Range) :
                j += i
                if i != j :
                    Length = int(self.DistanceTable.GetCellValue(i , j))
                    Arc = chr(65 + i) + chr(65 + j)
                    StartLengths.append(Length)
                    StartArcs.append(Arc)

        return (StartArcs, StartLengths)


    def Calculate(self , parent , StartArcs , StartLengths) :
        nodes = ""
        (OriginalArcs, OriginalLength) = Bubble(StartArcs , StartLengths)

        for i in range(len(OriginalArcs)) :
            first, second = OriginalArcs[i][0] , OriginalArcs[i][1]
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

        return ("The range is : " + str(LowerBound) + " < Optimal solution <= " + str(UpperBound))


    def SyncTable_GetLocation(self , event) :
        x = event.GetRow()
        y = event.GetCol()
        Numb = self.DistanceTable.GetCellValue(x , y)
        self.DistanceTable.SetCellValue(y , x , Numb)
        self.DistanceTable.RefreshAttr(y , x)




app = wx.App()

Frame1 = GetNumbOfVertex(None)
Frame1.Show()

# start the applications
app.MainLoop()
