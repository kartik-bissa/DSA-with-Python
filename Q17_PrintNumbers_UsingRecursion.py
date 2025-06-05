#To print numbers 1 to 5 Using Recursion
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n) 

print_numbers(5)