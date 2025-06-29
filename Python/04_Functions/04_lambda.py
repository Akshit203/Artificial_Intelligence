# A lambda function is a small, anonymous (nameless) function in Python that is defined using the lambda keyword.
# It can have any number of arguments but only one expression.


new_lambda = lambda x,y : x ** y
print(new_lambda(2,3))

add = lambda a, b : a + b
print(add(10,5))

max_num = lambda x,y : x if x > y else y
print(max(10,9)) 

