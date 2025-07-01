'''
    write a program to findout who has score maximum runs from given 3 player run 
'''
player1 = input("enter 1st player name")
player1_run = int(input("enter 1st player runs"))

player2 = input("enter 2nd player name")
player2_run = int(input("enter 2nd player runs"))

player3 = input("enter 3rd player name")
player3_run = int(input("enter 3rd player runs"))

#nested decision making 
if player1_run>player2_run:
    if player1_run>player3_run:
        print(f"{player1} has scored maximum {player1_run} run case 1")
    else:
        print(f"{player3} has scored maximum {player3_run} run case 2")
else:
    if player2_run>player3_run:
        print(f"{player2} has scored maximum {player2_run} run case 3")
    else:
        print(f"{player3} has scored maximum {player3_run} run case 4")

print("good bye")
            