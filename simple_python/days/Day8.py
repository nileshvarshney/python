""" Print each element of the list"""
pets = ['cat','dog','fish','bird','rabit','neighbor']

for pet in pets:
    print(pet)

# while loop testing
i_need_more_money=20
while  i_need_more_money < 35:
    print("Now I have ",i_need_more_money)
    i_need_more_money += 1

# Write a program that guess a number between 1 to 10
import random
counter = 0
target_numnber, guess_number=random.randint(1,10),3

while target_numnber != guess_number:
    target_numnber, guess_number=random.randint(1,10),3
    print ("Keep Guesting - ", counter,target_numnber, guess_number)
    counter += 1

