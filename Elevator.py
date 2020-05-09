import time
#items = []

def print_pause(message):
    print(message)
    time.sleep(1)

def first_floor(items):
    floor = "lobby"
    print_pause(f'You pushed the button for the first floor.\nAfter a few moments you find yourself in the {floor}.')
    if "ID Card" in items:
        print_pause("The clerk greets you, but she has already "
            "given you your ID Card, so there is nothing "
            "more to do here now.")
    else:
        print_pause("The clerk greets you and gives you an ID Card")
        items.append("ID Card")
    print_pause("You head back to the elevator")
    floor_input(items)

def second_floor(items):
    floor = "human resources"
    print_pause(f'You pushed the button for the second floor.\nAfter a few moments you find yourself in the {floor}.')
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem much to do here.")
    else:
        print_pause("The head of HR greats you.")
        if "ID Card" in items:
            print_pause("He look at your ID card and then"
                            " gives you a copy of the handbook")
            items.append("handbook")
        else:
            print_pause("He has something for you, but said he can't "
                            "give it to you until you get your ID Card.")
    print_pause("You head back to the elevator")
    floor_input(items)

def third_floor(items):
    floor = "engineering department"
    print_pause(f'You pushed the button for the third floor.\nAfter a few moments you find yourself in the {floor}.')
    print_pause("This is where you work!")
    if "ID Card" in items:
        print_pause("Use your ID card to open the door.")
        print_pause("Your program manager greets you and tells you that"
                        " you need to have a copy of the "
                        "employee handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job "
                            "as vice president of engineering!")
        else:
            print_pause("They scowl when they see that you don't have it, "
                            "and send you back to the elevator.")
            floor_input(items)
    else:
        print_pause("Unfortunately, the door is locked "
                        "and you can't get in.")
        print_pause("It looks like you need some kind of "
                        "key card to open the door.")
        print_pause("You head back to the elevator.")
        floor_input(items)
    
    
    
def floor_input(items):
    print_pause("Please enter the number for the floor you would like to visit:")
    floor = input(  "1. Lobby\n"
                    "2. Human Resources\n"
                    "3. Engineering department\n\n")
    if floor == '1':
        first_floor(items)
    elif floor == '2':
        second_floor(items)
    elif floor == '3':
        third_floor(items)
            
    print_pause("Where would you like to go next?")
    

def intro():
    print_pause("You have just arrived at your new job")
    print_pause("You are in the elevator")
    

def play_game():
    items = []
    intro()
    floor_input(items)

play_game()


