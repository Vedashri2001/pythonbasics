import random
roll_count=int(input("How many dice are we rolling?"))
sides=int(input("How many sides on each die?"))
while True:
    result="|"
    for die in range(roll_count):
        random1=random.randint(1,sides)
        result+=f"{random1}|"
    print(result)
    reply=input("Roll again?('q' to quit)")
    if reply=='q':
        break






