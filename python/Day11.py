# Accept a string and count the alpha and numbers in the string
input_string = input("Enter a alpha numeric strings :\t")
a,d = 0,0
for c in input_string:
    if c.isalpha():
        a += 1
    elif c.isdigit():
        d += 1
    else:
        pass
print('alpha :',a)
print('digit :',d)

""" 
validate supplied password for
 At least 1 [a-z]
 At least 1 [A-Z]
 At Least 1 [0-9]
 At least 1 [special chat]
 min length = 6
 max length = 16
"""

import re  # regular operation for matching operation
def password_check(password):   
    if (len(password) < 6 or len(password) > 16):
        return False
    elif not re.search('[a-z]',password):
        return False
    elif not re.search('[A-Z]',password):
        return False
    elif not re.search('[0-9]',password):
        return False
    elif not re.search('[#@$]',password):
        return False
    else:
        return True

#-------------------------------------------------------------------------------
# password main calling program
#-------------------------------------------------------------------------------
MAX_TRY = 3

counter = 1

for i in range(MAX_TRY):
    if (i == 0):
        password_string = input("Please supply password:\t")
    else:
        print('Supplied password is not enough strong...try again')
        password_string = input("Please supply password:\t") 

    test_result = password_check(password_string)
    if test_result:
        print('Password test successful')
        break

