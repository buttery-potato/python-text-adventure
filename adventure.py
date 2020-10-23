import time
import random
def repeat():
    while True:
        repeat=input("Would you like to play again?").lower()
        if repeat=="yes" or "y":
            game()
        elif repeat=="no" or "n":
            input("Press ENTER to exit.")
            exit()
        else:
            input("Sorry, I couldn't understand that. Press ENTER to exit.")
            exit()
def game():
    houses=["red", "orange", "yellow", "white", "beige", "purple", "brown"]
    randomHouse=random.choice(houses)
    oldWomanResponses=["you stutter and she slams the door on you.", "you say you're a character in a text adventure and she slams the door on you."]
    randomOldWomanResponse=random.choice(oldWomanResponses)
    begin=input("Would you like to begin? (Yes/No)").lower()
    if begin=="yes" or begin=="y":
        print("Great!\nYou cross the street.")
        time.sleep(1)
    elif begin == "no" or begin=="n":
        input("Ok. Maybe another time.\nPress ENTER to exit ")
        exit()
    direction=input("Which way? (North or South) ").lower()
    turn=input("Would you like to turn left or right? ").lower()
    # Code for north and left--with full north
    if direction=="north" and turn=="left":
        print("You turn north and then left.")
        print(f"You see many houses. The one that stands out most to you is the {randomHouse} one. You knock on the door, and an old woman answers the door. When she asks what you want, {randomOldWomanResponse}")
        repeat()
    # Code for north and left--with shortened north
    if direction=="n" and turn=="left":
        print("You turn north and then left.")
        print(f"You see many houses. The one that stands out most to you is the {randomHouse} one. You knock on the door, and an old woman answers the door. When she asks what you want, {randomOldWomanResponse}")
        repeat()
    # Code for north and right--with full north
    if direction=="north" and turn=="right":
        print("You turn north and then right.")
        print(f"You see many houses. The one that stands out most is the {randomHouse} one. You knock on the door, and an old man opens the door. When you tell him you are a character in a text adventure, he invites you in for a coffee.")
        repeat()
    # Code for north and right--with shortened north
    if direction=="n" and turn=="right":
        print("You turn north and then right.")
        print(f"You see many houses. The one that stands out most is the {randomHouse} one. You knock on the door and an old man opens the door. When you tell him you are a character in a text adventure, he invites you in for a coffee.")
        repeat()
    # Code for south and left--with full south
    if direction=="south" and turn=="left":
        print("You turn south and then left.")
        print(f"You see many houses. The one that stands out most to you is the {randomHouse} one. When you knock on the door, a child, no older than 7, opens the door. Against your better judgment, you ask if you can talk to his parents.")
        print("The child yells \"Mommy! Someone wants to see you!\" You hear footsteps and then a woman appears. She says \"Hello there! What's the problem?\"")
        print("You stutter and tell her that there's nothing wrong, you just wanted to see if everyone's OK. She assures you that everyone is OK, and then she shuts the door.")
        repeat()
    # Code for south and left--with shortened south
    if direction=="s" and turn=="left":
        print("You turn south and then left.")
        print(f"You see many houses. The one that stands out most to you is the {randomHouse} one. When you knock on the door, a child, no older than 7, opens the door. Against your better judgment, you ask if you can talk to his parents.")
        print("The child yells \"Mommy! Someone wants to see you!\" You hear footsteps and then a woman appears. She says \"Hello there! What's the problem?\"")
        print("You stutter and tell her that there's nothing wrong, you just wanted to see if everyone's OK. She assures you that everyone is OK, and then she shuts the door.")
        repeat()
    # Code for south and right--with full south
    if direction=="south" and turn=="right":
        print("You turn south and then right.")
        print(f"You see many houses. The one that stands out most to you is the {randomHouse} one. When you knock on the door, a man, probably 30 years old, opens the door. He says \"I'm sorry, but I'm not interested.\" You try to tell him \"No, no you've got it all wrong!\" but he's already closed the door.")
        repeat()
    # Code for south and right--with shortened south
    if direction=="s" and turn=="right":
        print("You turn south and then right.")
        print(f"You see many houses. The one that stands out most to you is the {randomHouse} one. When you knock on the door, a man, probably 30 years old, opens the door. He says \"I'm sorry, but I'm not interested.\" You try to tell him \"No, no you've got it all wrong!\" but he's already closed the door.")
        repeat()
game()
