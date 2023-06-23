import time
import random

def print_pause(message):
    print(message)
    time.sleep(2)

def fork_in_the_road():
    global score
    print_pause("\nYou find yourself standing at a fork in the road.")
    print_pause("To the left, the path appears to lead through a dense forest, while to the right, the path winds its way up a steep hill.")
    while True:
        choice = input("Which direction will you choose? (1) Go left or (2) Go right? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nNo matter which option you choose, you find yourself walking for what seems like hours.")
                print_pause("The forest grows thicker and darker.")
                score += random.randint(5, 15) # Add a random score bonus between 5-15 points
                break
            elif choice == 2:
                print_pause("\nNo matter which option you choose, you find yourself walking for what seems like hours.")
                print_pause("The hill becomes steeper and more treacherous.")
                score -= random.randint(5, 15) # Add a random score penalty between 5-15 points
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

def follow_the_stream():
    global score
    print_pause("\nNo matter which option you choose, you eventually come across a clearing in the woods.")
    print_pause("In the center of the clearing, you see a small, weather-beaten house.")
    while True:
        choice = input("Will you (1) approach the house or (2) stay in the clearing? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nNo matter which option you choose, you eventually find yourself standing in front of the house.")
                print_pause("You knock on the door, but no one answers.")
                score += random.randint(10, 20) # Add a random score bonus between 10-20 points
                break
            elif choice == 2:
                print_pause("\nYou stay in the clearing for a while, enjoying the peaceful surroundings.")
                score -= random.randint(5, 10) # Add a random score penalty between 5-10 points
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

def climb_the_mountain_range():
    global score
    print_pause("\nYou walk for what seems like hours, the scenery changing around you with every step.")
    print_pause("The forest begins to thin out, and you can see the sun shining through the trees ahead.")
    print_pause("As you emerge from the forest, you find yourself standing at the foot of a massive mountain range.")
    while True:
        choice = input("Will you (1) climb the mountain range or (2) circle around the mountain range? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nNo matter which option you choose, you eventually find yourself standing at the top of the mountain range, gazing out over the breathtaking vista below.")
                print_pause("You feel a sense of accomplishment and satisfaction at having overcome the challenge before you.")
                score += random.randint(20, 30) # Add a random score bonus between 20-30 points
                break
            elif choice == 2:
                print_pause("\nYou circle around the mountain range, taking in the stunning views along the way.")
                score -= random.randint(5, 10) # Add a random score penalty between 5-10 points
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

def visit_the_village():
    global score
    print_pause("\nAs you make your way down the other side of the mountain range, you come across a small village nestled in a valley.")
    while True:
        choice = input("Will you (1) stay in the village or (2) continue on your journey? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nYou spend a few days in the village, getting to know the friendly locals and enjoying their hospitality.")
                score += random.randint(30, 40) # Add a random score bonus between 30-40 points
                break
            elif choice == 2:
                print_pause("\nYoucontinue on your journey, eager to see what lies ahead.")
                score -= random.randint(10, 20) # Add a random score penalty between 10-20 points
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

def play_game():
    while True:
        global score
        score = 0
        print_pause("Welcome to Adventure Game, where you will embark on an exciting journey full of twists and turns!")
        print_pause("Your goal is to reach the end of the game with the highest score possible.")
        fork_in_the_road()
        follow_the_stream()
        climb_the_mountain_range()
        visit_the_village()
        print_pause(f"\nCongratulations on completing the game with a final score of {score} points!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() != "y":
            print_pause("Thank you for playing Adventure Game!")
            break

play_game()
