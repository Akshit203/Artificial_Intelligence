# ques 1 
password = "security@12345"

password_length = len(password)

if password_length < 8 :
    strength = "Weak"
elif password_length < 10 :
    strength = "Medium"
else :
    strength ="Strong"

print("Password strength is ", strength)



#ques 2
year = 2018

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print( year, " is a leap year")
else:
    print(year, "is not a leap year")
