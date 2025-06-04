def binary_search(arr,key):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        elif key <  arr[mid]:
            high = mid - 1
        else:
            low = mid +1

    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16]
key = 10
result = binary_search(arr,key)

if result != -1:
    print(f"{key} found at index {result}")
else:
    print(f"{key} not found")