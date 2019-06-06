import random 
print("Welcome to Game !")
i = int(input("Enter 0 to exit or Enter 1 to continue: "))
while i != 0:
    user_input = int(input("Choose Rock[0] , Scissor[1] or Paper[2] : "))
    Ai_input = random.randint(0,2)
    game = [user_input,Ai_input]
    if game == [0,2] or game == [1,0] or game == [2,1] :
        print("AI wins !")
    else:
        print("You WIN !")
print("Game End :( !")
