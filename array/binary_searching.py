def selectionSortedArray(arr):
    l = len(arr)
    for i in range(l):

        min_idx = i 

        for j in range(i+1, l):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp

    
    return arr

def binarySearch(arr, key):
    arr = selectionSortedArray(arr)
    print(f"After Sorting:\n {arr} ", )
    s = 0
    e = len(arr)

    while (s <= e):


        mid = (s + e) // 2

        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            e = mid -1 
        else:
            s = mid + 1

    return None
   


if __name__ =='__main__':
    arr = [1,9,2,4,7]
    key = 7
    print(binarySearch(arr, key))