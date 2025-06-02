#TO count how many numbers are even in given array
my_array=[1,2,4,6,7,9,28,55,3,22,11]
count=0 #initially zero elements are even
for numbers in my_array:
    if numbers % 2 == 0:
        count += 1 #count = count+1

print("Total number of even numbers in array is: ", count)