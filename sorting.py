def bubbleSort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        for j in range(len_arr-i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def selectionSort(arr):
    len_arr = len(arr)
    for i in range(0, len_arr):
        smallest_idx = i
        for j in range(i, len_arr):
            if arr[j]<arr[smallest_idx]:
                smallest_idx = j
        if i==smallest_idx:
            pass
        else:
            temp = arr[i]
            arr[i] = arr[smallest_idx]
            arr[smallest_idx] = temp
    return arr

def insertionSort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        if arr[0]>arr[i]:
            arr[:i+1] = [arr[i], *arr[:i]]
        else:
            for j in range(1, i):
                if (arr[i]>arr[j-1]) and (arr[i]<arr[j]):
                    arr[:i+1] = [*arr[:j], arr[i], *arr[j:i]]
                    break
    return arr

# Divide and Conquer                
def mergeSort(arr):
    len_arr = len(arr)
    if len_arr==1:
        return arr
    else:
        left = arr[:len_arr//2]
        right = arr[len_arr//2:]
        return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend([*left[i:], *right[j:]])
    return result

def quickSort(arr):
    pass
    
