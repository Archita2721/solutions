# Problem 1: Program to count occurrences of a given character in a string.

#  Count character 'e' in the below string.
# 	Input "geeksforgeeks". 
# 	Output: 4

# 	Count character '3' in the below string.
# 	Input "abccdefgaa."
# 	Output : 3

def count_character(input_string, character_to_count):
    count = 0
    for char in input_string:
        if char == character_to_count:
            count += 1
    return count

input1 = "geeksforgeeks"
character1 = 'e'
output1 = count_character(input1, character1)
print(f"Output: {output1}")

input2 = "abccdefgaa."
character2 = '3'
output2 = count_character(input2, character2)
print(f"Output: {output2}")