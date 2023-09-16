# Problem 2:  Determine whether a given string is Palindrome
# A string “madam” is a palindromic string because it reads the same forwards and backward. 
# Input: “anna”
# Output: true

# Input: “India”
# Output: false

def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]


input1 = "anna"
output1 = is_palindrome(input1)
print(f"Output: {output1}")

input2 = "India"
output2 = is_palindrome(input2)
print(f"Output: {output2}")
