# reduce() Reduces the list to a single value using a function.
# Returns a single value

# reduce() is not built-in function
# we must import it from the functools module like this: from functools import reduce


from functools import reduce

# Ex 1 :

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_result)  # Sum of numbers: 15

# Ex2 : Sum of even numbers :

from functools import reduce

numbers2 = [1, 2, 3, 4, 5, 6]
res = []

def isEven():
    for i in numbers2:
        if i % 2 == 0:
            res.append(i)
    return res

print("Even numbers are:", isEven()) 

def addEven(x, y):
    return x + y

addEven1 = reduce(addEven, res)
print("Sum of even numbers:", addEven1)




