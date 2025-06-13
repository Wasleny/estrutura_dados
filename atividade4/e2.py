def linear_search(arr):
    i = 0
    while arr[i] >= i + 1:
        i += 1
    
    return i
        
def binary_search(arr):
    return _binary_search(arr, 0, len(arr) - 1)

def _binary_search(arr, left, right):
    middle = (left + right) // 2

    if left > right:
        return left

    if arr[middle] >= middle + 1:
        return _binary_search(arr, middle + 1, right)
    
    if arr[middle] < middle + 1:
        return _binary_search(arr, left, middle - 1)
    
quotes = [12, 10, 9, 8, 6, 5, 4, 3] #5
print(linear_search(quotes))
print(binary_search(quotes))