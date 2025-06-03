#Count frequency of each character in a string
s = input("Enter a String: ")
#Yaha Dictonary use karenge(key=char,value=count)
freq={}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequencies: ")
for char in freq:
    print(f"{char} - {freq[char]}")