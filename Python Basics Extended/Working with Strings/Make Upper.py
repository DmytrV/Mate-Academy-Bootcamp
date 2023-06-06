# Write a function make_upper, which replaces all occurrences 
# of lowercase letters with uppercase in the text.

# Function has two parameters:

# text - a string in which you want to replace
# letter - a lowercase letter, all occurrences of which should 
# be replaced by a capital letter
# The function returns a list of two elements - 
# the modified string and the number of replacements that 
# have been made.

# Examples:

# make_upper("aaa", "a") == ["AAA", 3]
# make_upper("bBb", "b") == ["BBB", 2]
# make_upper("some long text", "e") == ["somE long tExt", 2]
# make_upper("aaabbabba", "b") == ["aaaBBaBBa", 4]

def make_upper(text: str, letter: str) -> list:
    occurrences = text.count(letter)
    new_text = text.replace(letter, letter.upper())
    return [new_text, occurrences]


print(make_upper("aaa", "a"))
print(make_upper("bBb", "b"))
print(make_upper("some long text", "e"))
print(make_upper("aaabbabba", "b"))