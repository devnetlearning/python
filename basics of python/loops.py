"""
for - loop that is making specific action for certain number of times.
range - set specific number of times. Allows to choose at which number starts
and how long do the loop
"""

"""
while - conditional loop
break - exiting the loop
"""















#while example1 - same function like in if statement but shorter and easier to expand

test = input(" What's your name?\n")
tries = 0
if test == "mark":
    print("Access Granted")
elif test != "mark":
    while(test != "mark"):
        print("Access deneid. Type your name again." ,2 - tries, "tries left")
        test = input(" What's your name?\n")
        if (tries >= 1 and test!="mark"):
            print("Access deneid. Contact with your admin")
            break
        tries = tries + 1
    else:
        print("Access granted")
