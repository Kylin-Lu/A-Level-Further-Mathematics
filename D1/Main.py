def EnterList():
    list = []
    while True:
        try:
            length = int(input("Please enter the length of the list : "))
            break
        except:
            print("Data type error .", end=" ")
    for i in range(length):
        while True:
            try:
                enter = int(input("Please enter the " + str(i + 1) + "th number : "))
                break
            except:
                print("Data type error .", end=" ")
        list.append(length)
    return list


def Bubble(list):
    for x in range(1, len(list)):
        for i in range(0, len(list) - x):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        print(list)
    return list


def Quick(list):
    if len(list) >= 2:
        front, back = [], []
        mid = list[len(list) // 2]
        list.remove(mid)
        for i in list:
            if i <= mid:
                front.append(i)
            else:
                back.append(i)
        return Quick(front) + [mid] + Quick(back)
    else:
        return list


def Shell(list):
    difference = int(len(list) / 2)
    while difference > 0:
        times = len(list) - difference
        for i in range(0, times):
            if list[i] > list[i + difference]:
                list[i], list[i + difference] = list[i + difference], list[i]
                print(list)
        difference = int(difference / 2)
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            print(list)


def Shuttle(array):
    for x in range(1, len(array)):
        if x % 2 != 0:
            for i in range(x // 2, len(array) - x // 2 - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
        else:
            for i in range(x // 2, len(array) - x // 2):
                if array[len(array) - i - 1] < array[len(array) - i - 2]:
                    array[len(array) - i - 2], array[len(array) - i - 1] = array[len(array) - i - 1], array[
                        len(array) - i - 2]
        print(array)
    return array


def Sort() :
    Case = {
        0 : Bubble(array)
    }
    type = ["Bubble" , "Quick" , "Shell's" , "Shuttle"]
    print(type)
    while True:
        try:
            choose = int(input("Please choose one type of sort on the list : "))
            break
        except:
            print("Data type error .", end=" ")
    while choose < 0 or choose > len(type) - 1 :
        print("Data out of list ." , end = " ")
        while True:
            try:
                choose = int(input("Please choose one type of sort on the list : "))
                break
            except:
                print("Data type error .", end=" ")
    array = EnterList()
