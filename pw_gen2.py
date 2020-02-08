'''
This project is about using a function to generate a password based on user's input on the password length. Default pw length is 8 characters.

The default pw format comprises of at least 1 upper case, 1 lower case, 1 digit and 1 special character.

User can also specify a list of special characters to be excluded.
'''
def pwgen(pwlen = 8, sc2ex = ''):
# Generate password according to the length given by the user. Default length is 8 characters
    pw = ''
    # Setup chars (upper case, lower case, numbers and special chars) in a string to be used for password.
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    # Remove chars defined by user not to be used with the random selection
    char = char.translate({ord(x): None for x in sc2ex})
    print(string.punctuation)
    print(char)
    # Randomly select chars from the 'adjusted' string to form password in accordance to the password length and return result.
    return ''.join(random.choice(char) for x in range(pwlen))

def pwcheck(pwd):
    # Return True when password format contains at least 1 upper cap, 1 lower cap, 1 special character and 1 digit
    f1 = f2 = f3 = f4 = False
    # Check each of the char of the pw to ensure format is valid
    for i in pwd:
        if 47 < ord(i) < 58: # Between 0 and 9
            f1 = True
        elif 64 < ord(i) < 91: # Between A and Z 
            f2 = True
        elif 96 < ord(i) < 123: # Between a and z
            f3 = True
        elif 32 < ord(i) < 48 or 57 < ord(i) < 65 or 90 < ord(i) < 97 or 122 < ord(i) < 127: # Special characters
            f4 = True
    if f1 == f2 == f3 == f4 == True:
        return True
    else:
        return False

# Keeps running until password contains at least 1 upper cap, 1 lower cap, 1 digit and 1 special character
import random
import string

scex = '_+-=[]\\}{|;:",./<>?' # Special chars to be excluded in the pw.
valid_pw  = False # Set the flag to false.
while valid_pw == False:
    pw = pwgen(10,scex) # In this example, pw length is 10 chars and should not inlude special chars defined in 'scex' variable.
    if pwcheck(pw) == True:
        validity = True # If pw format is correct, set flag to True

print('Password is ' + pw)
