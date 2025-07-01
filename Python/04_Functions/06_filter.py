# filter() function in Python is used to filter out elements from an 
# iterable (like a list, tuple,) based on a condition.

# Ex 1 : 

list1 = [1,2,3,4,5,6,7]

def test (n):
    return n > 5
    
x = filter(test, list1)

print(list(x)) # [6, 7]




# Ex 2 : 
def isEven (n):
    if n % 2 == 0:
        return n

even_number = filter(isEven, list1)

print(list(even_number)) # [2, 4, 6]




# Ex 3 : 
# using lambda with filter :

numbers = [10, 15, 21, 36, 45]

result = filter(lambda x: x % 3 == 0, numbers)
print(list(result))  # Output: [15, 21, 36, 45]




# Ex 4 : 
# Filter Non-Empty Strings :

num = [1,2,"",0, False, [], {}, ()]

res = filter(None, num)
print(list(res)) # [1,2]

# filter(None, iterable) explanation:
# It filters out all falsy values — that includes:
 
#   "" (empty string), 0, None, False, [], (), {} (empty containers)
# It keeps only the truthy values (like non-empty strings, non-zero numbers, etc.)







