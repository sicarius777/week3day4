# lets go

# Remove vowels
# Write a function that will remove all vowels from a given string. The function should return a string.
# Examples:                                                                 
# Input: 'Joel'
# Output: 'Jl'                                                     
# Input: 'Shoha'
# Output: 'Shh'

# def remove_vowel

# input
# define whhats a vowel
# identify the vows in a string
# have a for loop go through the string and remove the vowels
# return the string without the vowels

def vowel_removal(input_string):
    vowels = "aeiouAEIOU"
    out_put = []
    for char in input_string:
        if char not in vowels:
            out_put.append(char)
    return "".join (out_put)

            
            

print(vowel_removal("Joel"))

