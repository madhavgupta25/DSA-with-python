def partition(arr:list[int], s:int, e:int)->int:
    i = s
    j = s
    pivot = arr[e]

    while j<e:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j+=1
        else:
            j+=1

    arr[i], arr[e] = arr[e], arr[i]
    
    return i


def quicksort(arr:list[int], s:int, e:int)->None:
    #base case
    if s >= e: return


    p_idx = partition(arr, s, e)
    quicksort(arr, s, p_idx-1)
    quicksort(arr, p_idx+1, e)

arr =[60, 50, 20, 10, 40, 30]
n = len(arr)
quicksort(arr, 0 , n-1)
print(arr)

