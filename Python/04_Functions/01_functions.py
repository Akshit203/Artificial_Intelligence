def test():
    print("City Beautiful")

test() # City Beautiful

# test() + "Chandigarh" 
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

# Because test() returns None (default return of a function with no return statement)

# And we cannot concatenate NoneType with a string
# Hence, in most real-world use cases, we prefer using return instead of print inside functions

# Function with return — returns a string which can be used further

# --------------------------------------------------------------------------------------------------------------

def test2():
    return "City Beautiful"

print(test2() + " Chandigarh")  # Output: City Beautiful Chandigarh

# We use print() here because return value needs to be displayed or stored.

# we can also store it in a variable:
# result = test2()
# print(result)

# --------------------------------------------------------------------------------------------------------------

# Function returning multiple values of different data types
def test3():
    return "xyz", "abc", 12345, [10, 11, 12, 13]

print(test3())  
# Output: ('xyz', 'abc', 12345, [10, 11, 12, 13, 14, 15])
# This is a tuple containing mixed data types

# Unpacking the returned values into separate variables
a, b, c, d = test3()

print(a)  # Output: xyz
print(b)  # Output: abc
print(c)  # Output: 12345
print(d)  # Output: [10, 11, 12, 13, 14, 15]

# --------------------------------------------------------------------------------------------------------------

def test5():
    res = 5 + 2 / 7
    return res
print(test5()) # 5.285714285714286

# --------------------------------------------------------------------------------------------------------------


def test6(a,b,c):
    return a + b + c

res = test6(10,20,40) #70

res2 = test6("x", "y", "z") # xyz

res3 = test6([1,2,3,4],[100,101,102,103,104], [25552029301345]) # [1, 2, 3, 4, 100, 101, 102, 103, 104, 25552029301345]


print(res)
print(res2)
print(res3)