def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if (arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i] > target and i == 0:
            return 0
        if target > arr[i] and i == len(arr) - 1:
            return i + 1
        if target > arr[i] and arr[i + 1] > target:
            return i + 1
        
def binary_search(arr, target):
    return _binary_search(arr, target, 0, len(arr) - 1)

def _binary_search(arr, target, left, right):
    middle = (left + right) // 2

    if left > right:
        return left

    if arr[middle] == target:
        return middle
    
    if arr[middle] > target:
        return _binary_search(arr, target, left, middle - 1)
    
    if arr[middle] < target:
        return _binary_search(arr, target, middle + 1, right)


arr = [101, 10, 5, 12, 1, 3, 99, 25] #[1,3,5,10,12,25,99,101]
quicksort(arr)
print(linear_search(arr, 2))
print(binary_search(arr, 2))