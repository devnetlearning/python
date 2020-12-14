"""
for - loop that is making specific action for certain number of times.
range - set specific number of times. Allows to choose at which number starts
and how long do the loop
"""
#for example1 - print every number in range of 200 which could be devided
#by 5 but not by 7 without the remainder


for i in range(200):

    if ( i % 5 == 0 and i % 7 != 0):
        print (i)


#for example2 - multiplies each by each numbers between 2 provided values in set.


a = int(input(" 1st number: "))
b = int(input(" 2st number: "))
multiply = 1

for i in range (a,b+1):
    alist =[i]
    multiply = multiply * i

print(multiply)




"""
while - conditional loop
break - exiting the loop
"""

#while example - same function like in if statement but shorter and easier to expand

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
