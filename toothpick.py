player1=input("enter player 1's name:")
player2=input("enter player 2's name: ")
current_player=player1


no_of_toothpicks=13

while True:
    toothpic=" | " * no_of_toothpicks
    print(toothpic)
    print(f"there are {no_of_toothpicks} tooothpick left")
    choice=int(input(f"{current_player} how many toothpick do you want to take?"))
    while choice!=1 and choice!=2 and choice!=3:
        choice=int(input(f"invalid input please enter 1,2,3 :"))
    no_of_toothpicks-=choice
    if no_of_toothpicks<=0:
        print(f"{current_player}wins the game")
        break
    if current_player==player1:
        current_player=player2
    else:
        current_player=player1
    

print("Game over")
    
    
