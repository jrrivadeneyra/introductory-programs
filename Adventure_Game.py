import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def valid_input(prompt, opt1, opt2):
    while True:
        response = input(prompt).lower()
        if opt1 == response:
            break
        elif opt2 == response:
            break
    return response


def intro(AL):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it a {AL} is somewhere around here, "
                "and has been terrifying the near by village.\n")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand is your trusty "
                "(but not very effective) dagger.\n")


def search_input(IL, AL):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    search = valid_input("(Please Enter 1 or 2.)\n", '1', '2')
    if '1' == search:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens "
                    f"and out steps the {AL}.")
        print_pause(f"Eep! This is the {AL}'s house!")
        print_pause(f"The {AL} attacks you!")
        if "sword" in IL:
            action_input(IL, AL)
        else:
            print_pause("You feel a bit under prepared for this, "
                        "what with only having a dagger")
            action_input(IL, AL)
    else:
        if "sword" in IL:
            print_pause("You peer cautiously into the cave.")
            print_pause("You've already been here before, "
                        "and gotten all the good stuff. "
                        "It's just an empty cave now.")
            print_pause("You walk back to the field.\n")
            search_input(IL, AL)
        else:
            print_pause("You peer cautiously into the cave.")
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause("You have found the magic Sword of Orgoroth!")
            print_pause("You discard your silly dagger "
                        "and take the sword with you.")
            print_pause("You walk back to the field.\n")
            IL.append("sword")
            search_input(IL, AL)


def action_input(IL, AL):
    act = valid_input("Would you like to "
                      "(1) fight or (2) run away? ", '1', '2')
    if '1' == act:
        if "sword" in IL:
            print_pause(f"As the {AL} moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Orgoroth shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause(f"But the {AL} takes one look "
                        "at your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {AL}.  "
                        "You are victorious!")
        else:
            print_pause("You do your best... ")
            print_pause(f"but your dagger is not match for the {AL}")
            print_pause("You have been defeated!")
    else:
        print_pause("You run back into the field. "
                    "Luckily, you don't seem to have been followed\n")
        search_input(IL, AL)


def replay(IL):
    replay = valid_input("Would you like to play again? "
                         "(y/n)\n", 'y', 'n').lower()
    if replay == "n":
        print_pause("Thank you for playing! See you next time.")
    else:
        IL.clear()
        print_pause("Excellent! Restarting the game...\n")
        adventure_game()


def adventure_game():
    IL = []
    AL = ["dragon", "pirate", "gorgon", "troll", "wicked fairy"]
    actor = (random.choice(AL))
    intro(actor)
    search_input(IL, actor)
    replay(IL)


adventure_game()
