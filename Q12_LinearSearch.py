
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [2, 4, 6, 15, 23]
key = 15
result = linear_search(arr, key)
if result != -1 :
    print(f"{key} is found at index {result}")
else:
    print(f"{key} not found in array")