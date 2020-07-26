def countingSort(arr):
    my_dict = {}
    
    for i in range(0,100):
        my_dict[i] = 0
    
    for i in arr:
        my_dict[i] += 1
    
    final = []

    for i in my_dict:
        j = 0
        while j < my_dict[i]:
            final.append(i)
            j += 1
        
    return final
