import time
list = [8 , 7 , 14 , 9 , 6 , 9 , 5 , 15 , 6 , 7 , 8]
size = 20
def First_fit(list , size) :
    bins = [size]
    for i in range(0 , len(list)) :
        bin_num = 0
        if bins[bin_num] < list[i] :
            bins.append(size)
        while bins[bin_num] < list[i] :
            bin_num = bin_num + 1
        bins[bin_num] = bins[bin_num] - list[i]
        if bins[len(bins) - 1] == size :
            bins.remove(size)
    print(sum(bins) , "units are wasted .")
    return bins

def Decreasing(list , size) :
    list.sort(reverse = True)
    bins = [size]
    for i in range(0 , len(list)) :
        bin_num = 0
        if bins[bin_num] < list[i] :
            bins.append(size)
        while bins[bin_num] < list[i] :
            bin_num = bin_num + 1
        bins[bin_num] = bins[bin_num] - list[i]
        if bins[len(bins) - 1] == size :
            bins.remove(size)
    print(sum(bins) , "units are wasted .")
    return bins

start = time.clock()
print(First_fit(list , size))
end = time.clock()
print("Time taken :" , end - start)
start = time.clock()
print(Decreasing(list , size))
end = time.clock()
print("Time taken :" , end - start)