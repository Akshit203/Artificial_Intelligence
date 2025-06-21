# Nested if - else condition 

# Example 1  
age = 22
id_num = True

if age >= 20 :
    if id_num != False:
        print("you are allowed to enter")
    else :
        print("you Need to show ur Id")
else :
    print("Not allowed")


# Example 2
marks = 95

if marks >= 50 :
    if marks >= 90 :
        print("Grade A")
    elif marks >= 80 :
        print("Grade B")
    else :
        print("Grade C")
else :
    print("Fail")
