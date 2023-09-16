# Problem 3:  Biggest and smallest number in an array
# Write a program to print the biggest and smallest number in the array. 

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: Maximum is: 5
# Minimum is: 1

# Input: arr[] = {5, 3, 7, 4, 2}
# Output: Maximum is: 7
# Minimum is: 2

def find_max_and_min(numbers):
    if not numbers:
        print("The list is empty.")
        return

    max_number = numbers[0]  
    min_number = numbers[0]  

    for num in numbers:
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num

    print(f"Maximum is: {max_number}")
    print(f"Minimum is: {min_number}")


arr1 = [1, 2, 3, 4, 5]
find_max_and_min(arr1)

arr2 = [5, 3, 7, 4, 2]
find_max_and_min(arr2)
