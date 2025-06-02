#Take input from user and create array of 5 numbers
arr=[] #first we created an empty array
for i in range(5):
    num = int(input("Enter NUmber: "))
    arr.append(num)

print("Your array is: ",arr)