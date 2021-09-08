import time
array = [453 , 330 , 405 , 792 , 516 , 162 , 465 , 870 , 431 , 927 , 129 , 348 , 34 , 107 , 64 , 253 , 382 , 411 , 147 , 147 , 389 , 597 , 414 , 620 , 425 , 73 , 275 , 212 , 482 , 302 , 52 , 868 , 144 , 65 , 471 , 930 , 766 , 243 , 578 , 274 , 630 , 281 , 732 , 114 , 517 , 322 , 748 , 517 , 492 , 331]

def Shuttle(array) :
    for x in range(1 , len(array)) :
        if x % 2 != 0 :
            for i in range(x // 2, len(array) - x // 2 - 1) :
                if array[i] > array[i + 1] :
                    array[i] , array[i + 1] = array[i + 1] , array[i]
        else :
            for i in range(x // 2 , len(array) - x // 2) :
                if array[len(array) - i - 1] < array[len(array) - i - 2] :
                    array[len(array) - i - 2] , array[len(array) - i - 1] = array[len(array) - i - 1] , array[len(array) - i - 2]
        print(array)
    return array

start = time.clock()
print(Shuttle(array))
end = time.clock()
print("Time taken :" , end - start)