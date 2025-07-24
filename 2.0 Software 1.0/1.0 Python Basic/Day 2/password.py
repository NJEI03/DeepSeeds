password =input("Enter your password: ")
# lower_case = password.islower()
# upper_case = password.isupper()
# numeric = password.isnumeric()

# print(f"Lowercase: {lower_case}, Uppercase: {upper_case}, Numeric: {numeric}")
# if lower_case and upper_case and numeric:
#     print(" This Password is strong.")
# else: 
#     print("This Password is weak. Please try again.")
 

 #WE SHALL SET FLAGS FOR EACH CONDITION
lower_case = False
upper_case = False 
numeric=False
for char in password:
    if char.islower():
        lower_case = True
    elif char.isupper():
        upper_case= True
    elif char.isnumeric():
        numeric = True
if lower_case and upper_case and numeric:
    print("This Password is strong.")
else:   
    print("This Password is weak. Please try again.")        