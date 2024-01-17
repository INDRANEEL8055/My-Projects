password = input("enter the password: ")

result ={}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False    # to end loop when it becomes true
for i in password:
    if i.isdigit():
        digit = True  # THis will only be executed if we have a digit in password and the loop ends
result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["upper-case"] = uppercase

print(result)
if all(result.values()):
    print("strong password")
else:
    print("weak password")

