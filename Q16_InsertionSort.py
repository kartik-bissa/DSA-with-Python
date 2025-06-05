def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print(f'\nInserting {key} into sorted part')
        j = i - 1
        while j >= 0 and arr[j]>key:
            print(f'Shifting {arr[j]} to the right')
            arr[j+1] = arr[j]
            j -= 1 #j = j-1
        arr[j + 1] = key
        print("Array now: ",arr)

arr = [9,3,7,1,5]
insertion_sort(arr)
print(arr)