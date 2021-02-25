import random
#Random Numbers just to test my list "Skills"

pirateboat = [8, 36, 45, 68]

teavessel = [10, 40, 64]

#Training if's and elif's while using the "random" module.

if random.choice(teavessel) > random.choice(pirateboat):
    print("The tea vessel sucessfully escaped the pirates!")

elif random.choice(pirateboat) > random.choice(teavessel):
    print("The pirates captured the tea shipment!")


