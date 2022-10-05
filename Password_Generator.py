# random password generator (16 digit HEX)

# import the 'random' module

import random
import string

# if statement here to prompt user to say yes or no to a random generated password

inp = input('Would you like to generate a password? Type yes or no: ' + '\n')
if inp == 'yes':
    # this will just continue with the code
    ()
else:
    # this will exit the code
    print('Okay then, maybe some other time.')
    exit()

# random numbers
r_num1 = random.randint(0, 9); r_num2 = random.randint(0, 9)
r_num3 = random.randint(0, 9); r_num4 = random.randint(0, 9)
r_num5 = random.randint(0, 9); r_num6 = random.randint(0, 9)
r_num7 = random.randint(0, 9); r_num8 = random.randint(0, 9)

# random letters
r_let1 = random.choice(string.ascii_letters); r_let2 = random.choice(string.ascii_letters)
r_let3 = random.choice(string.ascii_letters); r_let4 = random.choice(string.ascii_letters)
r_let5 = random.choice(string.ascii_letters); r_let6 = random.choice(string.ascii_letters)
r_let7 = random.choice(string.ascii_letters); r_let8 = random.choice(string.ascii_letters)

# print random number and letter
num_1 = str(r_num1); num_2 = str(r_let1); num_3 = str(r_num2); num_4 = str(r_let2)
num_5 = str(r_num3); num_6 = str(r_let3); num_7 = str(r_num4); num_8 = str(r_let4)
num_9 = str(r_num5); num_10 = str(r_let5); num_11 = str(r_num6); num_12 = str(r_let6)
num_13 = str(r_num7); num_14 = str(r_let7); num_15 = str(r_num8); num_16 = str(r_let8)

# variables added together
passwd = num_1+num_2+num_3+num_4+num_5+num_6+num_7+num_8+num_9+num_10+num_11+num_12+num_13+num_14+num_15+num_16

print('Here is your 16 digit HEX password: ' + passwd)
print('Just copy and paste this into where you see fit, e.g. BitWarden')
