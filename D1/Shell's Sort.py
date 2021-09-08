import time
# def Shell(list) :
#     difference = int(len(list) / 2)
#     while difference > 0 :
#         for i in range(difference , len(list)) :
#             while i >= difference and list[i] < list[i - difference] :
#                 list[i] , list[i - difference] = list[i - difference] , list[i]
#                 i = i - difference
#                 print(list)
#         difference = int(difference / 2)
#     print(list)
list = [453 , 330 , 405 , 792 , 516 , 162 , 465 , 870 , 431 , 927 , 129 , 348 , 34 , 107 , 64 , 253 , 382 , 411 , 147 , 147 , 389 , 597 , 414 , 620 , 425 , 73 , 275 , 212 , 482 , 302 , 52 , 868 , 144 , 65 , 471 , 930 , 766 , 243 , 578 , 274 , 630 , 281 , 732 , 114 , 517 , 322 , 748 , 517 , 492 , 331]
def Shell(list) :
    difference = int(len(list) / 2)
    while difference > 0 :
        times = len(list) - difference
        for i in range(0 , times) :
            if list[i] > list[i + difference] :
                list[i] , list[i + difference] = list[i + difference] , list[i]
                print(list)
        difference = int(difference / 2)
    for i in range(0 , len(list) - 1) :
        if list[i] > list[i + 1] :
            list[i] , list[i + 1] = list[i + 1] , list[i]
            print(list)

start = time.clock()
Shell(list)
end = time.clock()
print("Time taken :" , end - start)