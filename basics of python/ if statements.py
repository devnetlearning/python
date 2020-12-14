
"""
If statements - sets comparasion to check if statement is true and do some action or
false and do another things.
elif - adds another logic check to the case.
if and elif makes action only if statement is true. In other case we must use
else.
else - if statement is false this will be executed.
"""

#example

test = input(" What's your name?\n")
if test == "Marek":
    print("Access Granted")
elif test == "marek":
    print("Access Granted")
else:
    print("Access Denied: Wrong name")
