# == INSTRUCTIONS ==
#
# These challenges are a bit trickier and, in some cases, will require a few
# lines of code. If you start to get a little stuck, take a step back and make
# a plan by breaking the overall task down into small steps.

# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
def starts_with_the_letter_a(string):
    capitalised = string.upper()
    if capitalised[0] == "A":
        return True
    return False


# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    capitalised = string.upper()
    if capitalised[-1] == "A":
        return True
    return False


# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    capitalised = string.upper()
    if "HELLO" in capitalised:
        return True
    return False


# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    # your code goes here (delete the pass below)
    capitalised = string.upper()
    index = capitalised.find("HELLO")

    if index!=-1:
        return (string[:index] + "goodbye" + string[index+5:])
    return string


# Purpose: removes the letter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
    return string.replace("x", "").replace("X", "")


# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    halfway = len(string)//2
    return string[:halfway]


# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    halfway = len(string)//2
    return string[halfway:]


# Congrats, you're done with this file. Move on to the next one.
