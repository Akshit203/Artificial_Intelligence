new_string = "Chandigarh"

# String Length :
print (len(new_string)) # 10

# access characters in a string using indexing :
print (new_string[2]) # a
print (new_string[0]) # c

# String Concatenation : 
str1 = "City"
str2 = "Beautiful"

result = str1 + " " + str2
print (result) # City Beautiful

# String Slicing :

str = "Chandigarh Panchkula Mohali"

print (len(str)) # 27
substring = str[0:12] # Chandigarh
print(substring)


# String Methods : Python provides many built-in methods for manipulating strings, 

text = "hello"
print(text.upper())  # Output: HELLO

text = "HELLO"
print(text.lower())  # Output: hello

text = "  xyz  "
print(text.strip())  # Output: 'xyz' strip() – Removes leading and trailing whitespaces

text = "Java C++ Javascript"
print(text.replace("Javascript", "Python"))  # Output: Java C++ Python

text = "1,2,3,4,5"
print(text.split(","))  # Output: ['1', '2', '3', '4', '5']
                        # split(separator) – Splits string into a list

text = "hello world"
print(text.find("world"))  # Output: 6

text = "abcabcxyzsjdiedsjsuejkdnaaklsmsaioeiodnm"
print(text.count("a"))  # Output: 5

text = "hello world" 
print(text.startswith("hello"))  # Output: True
                                 # Checks if string starts with a prefix

text = "photo.jpg"
print(text.endswith(".jpg"))  # Output: True
                              # endswith(suffix) Checks if string ends with a suffix

# isalpha() – Returns True if all characters are letters
print("Hello".isalpha())     # Output: True
print("Hello123".isalpha())  # Output: False

# isdigit() – Returns True if all characters are digits

print("12345".isdigit())     # Output: True
print("12a45".isdigit())     # Output: False

# 🔹 13. title() – Converts first letter of each word to uppercase
text = "python c++ reactjs nodejs javascript"
print(text.title())  # Output: Python C++ Reactjs Nodejs Javascript

# capitalize() – Capitalizes only the first letter of the string

text = "hello world"
print(text.capitalize())  # Output: Hello world

# swapcase() – Swaps case of all characters
text = "Hello WORLD"
print(text.swapcase())  # Output: hELLO world




