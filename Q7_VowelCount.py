s = input('Enter a string: ').lower()
vowels = 'aeiou'
count = 0
for char in s:
    if char in vowels:
        count += 1

print(f'The number of vowels is {count}')