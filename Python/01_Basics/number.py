import math
import random

print(1 < 2)

print (5 == 5)

print (5.0 != 5.25)

x = 2 
y = 3
z = 4

print (x < y < z) # True

print (x < y and y < z) # True

print (1 == 2 < 3) # False, because Python evaluates 1 == 2 < 3 like : (1 == 2) and (2 < 3)
 
print (1 == 2 and 2 < 3) # False

############################################################################################


print (math.floor(4.5)) # 4
print (math.floor(-4.5)) # -5

# math.trunc(x) returns the integer part of the number by truncating toward zero 

print (math.trunc(2.4)) # 2
print (math.trunc(-2.4)) # -2


print (random.random())

print (random.randint(1,200))

list1 = ["xyz", "abx", "ijk"]
print (random.choice(list1))

print (random.shuffle(list1)) # none
list1 = ["xyz", "abx", "ijk"]

print (random.shuffle(list1))
print (list1) # ['ijk', 'xyz', 'abx']


############################################################################################

print (0.1 + 0.1 + 0.1) 
# 0.30000000000000004 Binary approximation issue ?

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) # 0.3


############################################################################################


setone = {1,2,3,4,5,6,7}
settwo = {3,4,5,6,77,88,99}

print (setone & settwo) # {3, 4, 5, 6} intersection
print (setone | settwo) # {1, 2, 3, 4, 5, 6, 7, 99, 77, 88} union of sets

print (setone - {1,2,3,4,5,6,7}) # why set() but not {}
# because empty {} creates an empty dictionary, not an empty set. To create an empty set, we use set()

print (type ({})) # <class 'dict'>

print (type (True)) # <class 'bool'>