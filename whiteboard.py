# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# Write a function that returns the number (i.e., count) of vowels in a given string.

# For this exercise, consider the following as vowels: a, e, i, o, u. The letter 'y' is not considered a vowel.

# Constraints:

# The input string will only consist of lowercase letters and/or spaces.

string1 = 'asd asdafvs ed'

def is_vowel(astring):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for letter in astring:
        if letter not in vowel_list:
            pass
        else:
            vowel_count += 1
    return vowel_count

print(is_vowel(string1))


def vowel_counter(bstring):
    vowel_list2 = ['a', 'e', 'i', 'o', 'u']
    return len([letter for letter in vowel_list2])