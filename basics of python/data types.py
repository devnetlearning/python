

"""
               Unique elements     Order    Change of var    Adding new var
LIST                NO              YES          YES              YES
TUPLE               NO              YES           NO               NO
DICTIONARIES        YES              NO          YES              YES
SET                 YES              NO           NO              YES

"""



"""
- List - "[]" - Ordered sequence of Objects:

Can contain integers, strings, and even other lists.
Can contain variables which are equal.
Can add new elements and modify existing.
"""
#example - assigning list and simple operations
test = [Mark, Clark, James]

#input
lista = [1, 5, 7, 8, -2, "mark", "tim"]
lista.append(3)
print(lista)
#output
[1, 5, 7, 8, -2, 'mark', 'tim', 3]

#input
lista = [1, 5, 7, 8, -2, "mark", "tim"]
lista.insert(3,12)
print(lista)
#output
[1, 5, 7, 12, 8, -2, 'mark', 'tim']


#input
lista = [1, 5, 7, 8, -2, "mark", "tim"]
lista.pop(3)
print(lista)
#output
[1, 5, 7, -2, 'mark', 'tim']


"""
- Tuple - "()" - Orderer group of immutable objects:
test = ( 12 , Amy , student )
tuples can not be changed after defined.
Used when you are sure that variables won't change.
It's used in big application in order to save some memory.
"""
test = ( 12 , Amy , student )
"""
- Dictionary - "{}" - unordered key:value pairs:
build in system for storing data as key:value pairs. Assigning data to
the key and using it later. A value can be any Python object.
 order doesn't matter.
"""
#example - updating dictonary
#input
dictonary = {1:"Mark", 2:"Dean",3:"Carl"}
print(dictonary)
dictonary.update ({1:"Mathew"})
print(dictonary)
#output
{1: 'Mark', 2: 'Dean', 3: 'Carl'}
{1: 'Mathew', 2: 'Dean', 3: 'Carl'}

"""
- Set - "{}" - unordered group of unique objects:
Sets are created by putting variables between curly brackets
Can't change variables in set.
Can add new elements
Most commonly used to reduce duplicates
"""
seta = {1, 3, 2, 4, 6,}

#Example - converting list into set and printing same elements from each group of
#variables

lista = [1, 5, 7, 8, -2]
listb = [3, 5, 12, 8, 23, -2, 12]

print(set(lista)&(set(listb)))

#Example - printing all of the lista elements that listb do not contain
lista = [1, 5, 7, 8, -2]
listb = [3, 5, 12, 8, 23, -2, 12]

print(set(lista)-(set(listb)))


#Example1 - Dictonary into list

"""Converting dictionaries into list and adding new dictonary to existing
 list of dictonaries"""


#input
conf1 = { "interface": "FastEthernet 0/0",
              "ipadress": "192.168.1.1",
              "vlanid" : 2 }
conf2 = { "interface": "FastEthernet 0/1",
              "ipadress": "192.168.1.2",
              "vlanid" : 2 }
conf3 = { "interface": "FastEthernet 0/2",
              "ipadress": "192.168.1.3",
              "vlanid" : 2 }

config = [conf1,conf2,conf3]
config.append({"interface" : "FastEthernet 1/0","ip address":"192.168.1.4","vlanid" : 3 })
print(config)
#output
[{'interface': 'FastEthernet 0/0', 'ipadress': '192.168.1.1', 'vlanid': 2},
{'interface': 'FastEthernet 0/1', 'ipadress': '192.168.1.2', 'vlanid': 2},
{'interface': 'FastEthernet 0/2', 'ipadress': '192.168.1.3', 'vlanid': 2},
{'interface': 'FastEthernet 1/0', 'ip address': '192.168.1.4', 'vlanid': 3}]
