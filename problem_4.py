
# Problem 4:  Swap two Strings Without Using any Third Variable
# Input: a = "Hello", b = "World".
# Output: Strings after swap: a = World and b = Hello

def swap_strings(a, b):
    a = a + b  
    b = a[:len(a) - len(b)] 
    a = a[len(b):] 

    return a, b


a = "Hello"
b = "World"

print(f"Strings before swap: a = {a} and b = {b}")
a, b = swap_strings(a, b)
print(f"Strings after swap: a = {a} and b = {b}")
