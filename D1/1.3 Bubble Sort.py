#list = [453 , 330 , 405 , 792 , 516 , 162 , 465 , 870 , 431 , 927 , 129 , 348 , 34 , 107 , 64 , 253 , 382 , 411 , 147 , 147 , 389 , 597 , 414 , 620 , 425 , 73 , 275 , 212 , 482 , 302 , 52 , 868 , 144 , 65 , 471 , 930 , 766 , 243 , 578 , 274 , 630 , 281 , 732 , 114 , 517 , 322 , 748 , 517 , 492 , 331]

def Bubble(list) :
    for x in range(1 , len(list)) :
        for i in range(0 , len(list) - x) :
            if list[i] > list[i + 1] :
                list[i] , list[i + 1] = list[i + 1] , list[i]
        print(list)
    return list

list = [8,3,4,6,5,7,2]
print(Bubble(list))
