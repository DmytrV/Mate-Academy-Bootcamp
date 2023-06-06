# This morning we've received a letter from the Grand Mate Hotel.

# Long story short, the programmers have not changed the type of field "number of guests" in the booking form and they still receive the strings like Room for 4 guests, please, Exactly 2 people, Meh, I'll be alone. Managers suffer because they are forced to process such requests manually.

# I think we can help them. Let's improve the function calculate_guests to make it look for numbers in the middle of the string guests_input. If it is still impossible to determine the number of guests, or this number is equal to 0 - return not a number.

# Requirements:

# Get only integers from string, if there is a float number - float part should be omitted.
# If there is two separate integers in a string, get only the first one.
# Examples:

# calculate_guests("I think 5 guests") == 5
# calculate_guests("Big company of 15 dudes") == 15
# calculate_guests("5") == 5
# calculate_guests("alone") == "not a number"
# calculate_guests("0") == "not a number"
# calculate_guests("Hello, 9.75 people") == 9
# calculate_guests("There will be 7 or 9 guys") == 7
# calculate_guests("hello cat walks on my keyboard ksadjfhskaj12.34kasdfhsjk") == 12

from typing import Union


def calculate_guests(guests_input: str) -> Union[int, str]:
    number = ""
    for i in guests_input:
        if i.isdigit():
            number += i
        elif len(number) > 0:
            break
    if not len(number) or number == "0":
        return "not a number"
    return int(number)


print(calculate_guests("I think 5 guests"))
print(calculate_guests("Big company of 15 dudes"))
print(calculate_guests("5"))
print(calculate_guests("alone"))
print(calculate_guests("0"))
print(calculate_guests("Hello, 9.75 people"))
print(calculate_guests("There will be 7 or 9 guys"))
print(calculate_guests("hello cat walks on my keyboard ksadjfhskaj12.34kasdfhsjk"))