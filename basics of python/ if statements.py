
"""
If statements - sets comparasion to check if statement is true and do some action or
false and do another things.
elif - adds another logic check to the case.
if and elif makes action only if statement is true. In other case we must use
else.
else - if statement is false this will be executed.
"""

#example1

test = input(" What's your name?\n")
if test == "Marek":
    print("Access Granted")
elif test == "marek":
    print("Access Granted")
else:
    print("Access Denied: Wrong name")

#example2

test = input(" What's your name?\n")
tries = 1

if test == "mark":
    print("Access Granted")
elif test != "mark":
    print("Access Denied.",3 - tries,"tries left")
    tries = tries + 1
    test = input(" What's your name?\n")
    if test == "marek":
        print("Access Granted")
    elif test != "mark":
        print("Access Denied.",3 - tries,"tries left")
        tries = tries + 1
        test = input(" What's your name?\n")
        if test == "mark":
            print("Access Granted")
        elif test != "mark":
            print("Access Denied.Contact admin to log in")
            tries = tries + 1
