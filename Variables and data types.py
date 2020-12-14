"""
Variable - label mapped to the object.
Rules in assigning variables:
- Must start with letter or underscore character
- Can't strt with number.
- Name is case sensitive.
"""
#example

name = "mark" # Variable assigned to string
age = 9 # Variable assigned to integer
married = True #Variable assigned to Boolean
full name = name + " Smith" #Variable assigned to another variable


#Data types and operations:
"""
1.Mutable - allowed to be changed (Objects that will be edited):

- List - Ordered sequence of Objects:
Can contain integers, strings, and even other lists.
test = [Mark, Clark, James]

- Dictionary - unordered key:value pairs:
build in system for storing data as key:value pairs. Assigning data to
the key and using it later. A value can be any Python object.

- Set - unordered group of unique objects:

test = {1,3,5,7,8,9,0,1,2}
to join two sets without duplicates you should use pipe  "|"

2.Immutable - not allowed to be changed (Constant values that you don't want
to be changed)

- String - group of ordered characters ("Test" , "Mark" , "2020"):

    Even if string contain number it's still considered as character

    int("10") - convert string to integer

- Integer - number without decimal points ( 1 , 10 , 23)

- Float - number with decimal points (1.2 , 13.4 , 565.1312)

- Boolean - Compariasion value (True or False)

- Tuple - Orderer group of immutable objects:
test = ( 12 , Amy , student )

Build in operations for working with numbers:

 + - add
 - - subtract
 * - multiply
 / - divide
 // - integer division
 % - modulus
 ** - exponent

Compariasion operations:

< - Less than
> - Greater than
<= Less than or equal
>= Greater than or equal
== equal
!= not equal
"""
