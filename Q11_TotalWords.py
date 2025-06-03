#To count number of words in a sentence
sen = input('Enter sentence: ')
words = sen.split()
print(len(words))
#Now lets capitalize each word of sentece
capital = "" 
for word in words:
    capital += word[0].upper() + word[1:] + " "

print("Capitalized: ", capital.strip())
    