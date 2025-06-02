arr=[5,10,50,67,20,3]
largest = arr[0] #initially first element ko largest mana
for i in arr:
    if i > largest:
        largest=i

print(f"The Largest number in array is {largest}")