__author__ = 'Pneumatic'

# Write a script using the provided python files in the sidebar
# This script must loop until the user is finished
# This script has to have all the variables types
# This script has to use an if, else if, and else statement
# This script Must user 5 different types of operators
# Script must be something useful. In programming you can be given the material but it is up to you to create a program
# Have fun!
decision = "y"
while decision == "y":
    print("Welcome to Ancient Astronauts")
    print("You wake up in and get out of bed and are under attack by another ship and you can not tell who it is and\n"
          "you run to the caption to find him dead along with all of the other of your crew members you run to and\n"
          "escape pod and fly into a wormhole because that is you only hope of survival you fly to this planet that\n"
          "looks suitable for life and there you find a beautiful woman asleep and you decide to have sex with her\n"
          "iscase you end up dieing. The woman's name was Marry and you stay around long enough for the baby to be\n"
          "born and the baby is named Jesus. Soon after you go back up into space in your ship in search for another\n"
          "wormhole to send you back to your world.")
    print(" ")
    print("You have two choices to go North or West to the North there is a bright star and to\n"
          "the West there is three stars that remind you of a belt")
    print(" ")
    helps = input("Please type everything in lower case now please hit enter.")
    choice = input(">>> ")

    if choice == "north":
        print("The trip to the star is longer than you thought it would be and you realize your you ship\n"
              "is low on energy. To the west the is a blue planet and to the east there is a red planet\n"
              "you know either one has the right amount of radiation but you don't know about the life forms.")
    elif choice == "west":
        print("You travel to your ship is inline with the three stars you see a ship that looks a lot like\n"
              "One of the long distance fliers that was aboard your mothership so you hed in its direction\n"
              "hoping it would see you and pick you up.")
    choice = input(">>> ")

    if choice == "west":
        print("You arrive at the blue planet and as you are refueling you see a large ship so you walk over\n"
              "to it and see a large alien you do not know if it is friendly or not should you kill giant or\n"
              "try to befriend giant")
    elif choice == "east":
        print("As you try to land on the red planet you crash your ship but you are in luck there is a bigger\n"
              "nicer ship than your escape pod. You walk up to it and see an alien dwarf you do not know if it\n"
              "is friendly or not should you kill dwarf or try to befriend dwarf ?")
    choice = input(">>> ")

    if choice == "kill dwarf":
        print("Good job you killed the dwarf and took his ship")
    elif choice == "befriend dwarf":
        decision = input("The dwarf killed you. Game Over play again y/n")

    elif choice == "kill giant":
        decision = input("You failed to kill the giant and ended up dieing. Game Over would you like to play again y/n")
    elif choice == "befriend giant":
        print("The giant turned out to be really friendly and he allows you aboard his ship and he introduces you\n"
              "to his two friends who are dwarfs.")