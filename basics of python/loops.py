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


#for example3 - aritmetic average (compare with the same example using while)

values = 0
i = 0


for i in range(5):
    value = int(input(" Input value: "))
    if value > 0:
        values = values + value
        i += 1
    else:
            print("Value must be positive number" )
    continue
print(values/i)



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



#wghile example2 arithmetic average with loop while

values = 0
i = 0


while i < 5:
    value = int(input(" Input value"))
    if value > 0:
        values = values + value
        i += 1
    else:
            print("value must be positive number" )
    continue
print("arithmetic average: ", values/i)


#while example3 adding 3 positive and even numbers. Inform if numbor is not positive or even

summ = 0
i = 0

while i < 3:
    number = int(input("Number: "))
    if number % 2 == 0 and number > 0:
        summ = summ + number
        i += 1
    else:
            print(" This number is not even or positve. Try again")


print(" Sum: ", summ)



#while example4 guessing correct number. 3 tries to gues


number = 17
i = 0

print("You have 3 tries to guess the number")

while i <= 2:

    guess = int(input("Your number: "))
    i+=1
    if guess > number:
        print(" Wrong number. Correct number is lower!")
    elif guess < number:
            print(" Wrong number. Correct number is higher!")
    else:
            print(" Great! You guessed it")

if guess != number:
    print("Out of tries. You loose it!")
