import time
import math
def Binary(array , follow) :
    while len(array) > 2 :
        mid = math.ceil((len(array) + 1) / 2)
        new = []
        if array[mid] == follow :
            new.append(array[mid])
        elif follow > array[mid] :
            for i in range(mid , len(array)) :
                new.append(array[i])
        else :
            for i in range(0 , mid - 1) :
                new.append(array[i])
        array = new
        print(array)
    if follow == array[1] :
        print(array[1])
    elif follow == array[0] :
        print(array[0])
        return "The research is complete . \n" + follow + " has been found in the list ."
    else :
        return "The list has only one item which is not " + follow + " . \nTherefore " + follow + " is not in the list ."

array = ["Bush" , "Elizabeth" , "Kennedy" , "Trump" , "Obama"]
follow = "Kennedy"

start = time.clock()
print(Binary(array , follow))
end = time.clock()
print("Time taken :" , end - start)