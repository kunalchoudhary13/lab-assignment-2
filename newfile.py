user=input("username=")
print(user)
import re
pswrd= input("password")
x = True
while x:  
    if (len(pswrd)<6 or len(pswrd)>12):
        break
    elif not re.search("[a-z]",pswrd):
        break
    elif not re.search("[0-9]",pswrd):
        break
    elif not re.search("[A-Z]",pswrd):
        break
    elif not re.search("[$#@]",pswrd):
        break
    elif re.search("\s",pswrd):
        break
    else:
        print("Valid Password "%s)
        x=False
        break

if x:
    print("Not a Valid Password")
