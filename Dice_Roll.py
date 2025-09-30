import random

r = random

num = [1,2,3,4,5,6]
roll = r.choice(num)

print("You roll the dice and get a...")
print(roll)
if (roll == 6):
    print("You get one more roll for getting a 6...")
    print("You roll again and get a....")
    roll = r.choice(num)
    print(roll)
else:
    exit
