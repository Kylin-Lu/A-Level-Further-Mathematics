#list = [453 , 330 , 405 , 792 , 516 , 162 , 465 , 870 , 431 , 927 , 129 , 348 , 34 , 107 , 64 , 253 , 382 , 411 , 147 , 147 , 389 , 597 , 414 , 620 , 425 , 73 , 275 , 212 , 482 , 302 , 52 , 868 , 144 , 65 , 471 , 930 , 766 , 243 , 578 , 274 , 630 , 281 , 732 , 114 , 517 , 322 , 748 , 517 , 492 , 331]
def Quick(list) :
    if len(list) >= 2 :
        front , back = [] , []
        mid = list[len(list) // 2]
        list.remove(mid)
        for i in list :
            if i <= mid :
                front.append(i)
            else :
                back.append(i)
        return Quick(front) + [mid] + Quick(back)
    else :
        return list

list = [15,3,1,6,2,14,7]
print(Quick(list))