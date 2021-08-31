def countSort(arr):
    count_array = countingArr(arr)
    arr_sort = []

    for i in range(len(count_array)):
        for j in range(count_array[i]):
            arr_sort.append(i)

    return arr_sort

def countingArr(arr):
    count_array = []
    for i in range(max(arr) + 1):
        count_array.append(0)
    
    for j in arr:
        count_array[j] += 1
    
    
    return count_array


arr = [2, 3, 342, 43, 21, 87, 2, 43, 12, 23, 0, 21]
print(countSort(arr))