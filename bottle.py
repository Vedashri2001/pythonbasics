for bottle in range (100,0,-1):
    print(f"{bottle} bottles of beer on the wall,{bottle} bottles of beer.")
    if bottle==1:
        print("Take one down pass it around no more bottles of beer on the wall")
    else:
        print(f"Take one down pass it around {bottle-1 } bottles of bear on the wall")
    print("*" * 50)