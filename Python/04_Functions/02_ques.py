# Extract integers from the given list and store them in a new list

list1 = ["xyz", "abx", 1, 2, 3, 4, 5, 6, [200,400,600,800]]

def extract_integers(input_list):
    result = []
    for i in input_list:
        if type(i) == int:
            result.append(i)
    return result

print(extract_integers(list1))  # Output: [1, 2, 3, 4, 5, 6]

# Extract all integers from the given list, including from nested lists

def extract_int2(input_list):
    result2 = []
    for i in list1:
        if type(i) == list:
            for j in i :
                result2.append(j)
        else :
            if type(i) == int or type(i) == float:
                result2.append(i)
    return result2

print(extract_int2(list1)) # [1, 2, 3, 4, 5, 6, 200, 400, 600, 800]
