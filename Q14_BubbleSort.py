def bubble_sort(arr):
    n = len(arr)
    for i in range(n): #Number of passses
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [5, 3, 4, 1]
bubble_sort(arr)
print("Sorted Array: ",arr)