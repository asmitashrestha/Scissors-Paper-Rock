import random

user_count=0
computer_count=0

options =["scissors","paper", "rock"]

while True:
    user_input =input("Type scissors/paper/rock or quit :")
    if user_input =="q":
        break

    if user_input not in options:
        continue

    random_number =random.randint(0,2)
    #scissor=0,paper=1, rock=2
    computer_input=options[random_number]
    print("Computer Input",computer_input+".")

    if user_input=="scissors" and computer_input == "paper":
        print("you won the game!!")
        user_count+=1

    elif user_input=="paper" and computer_input == "rock":
        print("You won the game!!")
        user_count+=1  

    elif user_input == "rock" and computer_input == "scissors": 
        print("You won the game!!")
        user_count+=1

    else:
        print("You lost the game!!")
        computer_count+=1        

print("You won the game ",user_count,"times.")
print("The computer won the game",computer_count,"times.")
print("Thank you for playing!!")
