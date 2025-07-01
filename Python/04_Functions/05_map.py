list1 = [10,20,30,40,50]

def test1():
    res = []
    for i in list1:
        res.append(i*i)
    return res
          
print(test1()) # [100, 400, 900, 1600, 2500]


# using map function :

def sqr(n):
    return n*n

res1 = map(sqr,list1)
print(list(res1)) # [100, 400, 900, 1600, 2500]


# Convert a list of strings to uppercase using map()

words = ['xyz', 'abc', 'ijk']
def uppercase1 (n):
    return n.upper()

res2 = map(uppercase1, words)
print(list(res2)) # ['XYZ', 'ABC', 'IJK']

# Get the length of each word in a list

words1 = ['python', 'java']

def length(n):
    return len(n)

x = map(length, words1)
print(list(x))


