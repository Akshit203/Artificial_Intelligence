"""
A generator function in Python is a special type of function that allows you to 
iterate over data one item at a time without storing the entire sequence in memory.

It uses the yield keyword instead of return.
Memory-efficient (especially for large data sets).

Real Use Cases : Reading large files line by line, Streaming data (APIs, logs, etc.)

"""

def test_gen(n):
    a, b = 0, 1

    for i in range (n):
        yield a
        a, b = b, a + b

for i in test_gen(10):
    print(i)


def test_gen2(n):
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

itr = test_gen2(10)

for i in range(10):
    print(next(itr))

# iter() and next() explained :

list = [1,2,3,4,5,6,7]

itr = iter(list)

print(next(itr)) # 1
print(next(itr)) # 2
print(next(itr)) # 3
print(next(itr)) # 4
print(next(itr)) # 5
print(next(itr)) # 6
print(next(itr)) # 7

# Meaning of Iterable in Python :

# An object is called an iterable if it can return its elements one at a time, 
# allowing it to be looped over in a for loop.

# Iterable Objects :
# list, tuple, str, set, dict, range, file, generator, etc.

# Non - iterable Objects :
# int, float, bool, function, Nonetype














def test(n):

    a = 0
    b = 1
    res = []

    for i in range(n):
        res.append(a)
        a, b = b, a + b
    return res

    
print(test(10))
