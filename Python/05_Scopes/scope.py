user = "Xyz"   # Global variable

def test():
    user = "ABC"  # Local variable (specific to function `test`)
    print(user)   # prints local value: "ABC"

print(user)      # Output: Xyz (global remains unchanged)
test()           # Output: ABC


