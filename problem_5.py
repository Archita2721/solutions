#  Problem 5: Swap two numbers without using a temporary variable
#  Input:integer a = "10", b = "50".
#  Output: Strings after swap: a = 50 and b = 10


a = 10
b = 50

print(f"Numbers before swap: a = {a} and b = {b}")

a = a + b
b = a - b
a = a - b

print(f"Numbers after swap: a = {a} and b = {b}")
