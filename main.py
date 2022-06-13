import random
params = ["R", "P", "S"]
dic = {"R":"Rock", "P": "Paper", "S":"Scissors"}
decorate = "***************"

def comp_decide():
    global comp_choice
    comp_choice = random.choice(params)
    return comp_choice


def enter_input():
    print("Choose one:")
    global User_input
    User_input = input("\"R\" for \"Rock\" \n \"P\" for \"Paper\" \n \"S\" for \"Scissors\" \n Enter here:  ").upper().strip(" ")
    return User_input


def is_valid():
    global valid
    if User_input in params:
        valid = True
    else:
        valid = False
        print("Invalid Entry")


def find_win():
    while valid is True:
        if User_input == comp_choice:
            print("Computer:", dic[comp_choice], "\nYou:",
            dic[User_input])
            print(decorate,"Tie", decorate)
            play_again()
            break
        elif (User_input == "S" and comp_choice == "R") or (User_input == "P" and comp_choice == "S") or (User_input == "R" and comp_choice == "P"):
            print("Computer:", dic[comp_choice], "\nYou:",
                  dic[User_input])
            print(decorate,"Computer wins",decorate)
            play_again()
            break

        else:
            print("Computer:", dic[comp_choice], "\nYou:",
                  dic[User_input])
            print(decorate,"You win", decorate)
            play_again()
            break
    else:
        enter_input()
        is_valid()
        find_win()

def play_again():
    print("Do you want to play again?")
    response = input("Y or N:  ").upper().strip(" ")
    if response == "Y":
        enter_input()
        is_valid()
        find_win()
    else:
        print("Thank you for playing.")

comp_decide()
enter_input()
print(is_valid())
find_win()
