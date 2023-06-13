import time
import random


def fork_in_the_road():
    global score
    print("You find yourself standing at a fork in the road.")
    time.sleep(2)
    print("To the left, the path appears to lead through a dense forest, while to the right, the path winds its way up a steep hill.")
    time.sleep(2)
    while True:
        choice = input("Which direction will you choose? (1) Go left or (2) Go right? ")
        if choice == "1":
            print("No matter which option you choose, you find yourself walking for what seems like hours.")
            time.sleep(2)
            print("The forest grows thicker and darker.")
            score += random.randint(5, 15) # Add a random score bonus between 5-15 points
            break
        elif choice == "2":
            print("No matter which option you choose, you find yourself walking for what seems like hours.")
            time.sleep(2)
            print("The hill becomes steeper and more treacherous.")
            score -= random.randint(5, 15) # Add a random score penalty between 5-15 points
            break
        else:
            print("Invalid choice, please try again.")

def follow_the_stream():
    global score
    print("No matter which option you choose, you eventually come across a clearing in the woods.")
    time.sleep(2)
    print("In the center of the clearing, you see a small, weather-beaten house.")
    while True:
        choice = input("Will you (1) approach the house or (2) stay in the clearing? ")
        if choice == "1":
            print("No matter which option you choose, you eventually find yourself standing in front of the house.")
            time.sleep(2)
            print("You knock on the door, but no one answers.")
            score += random.randint(10, 20) # Add a random score bonus between 10-20 points
            break
        elif choice == "2":
            print("You stay in the clearing for a while, enjoying the peaceful surroundings.")
            score -= random.randint(5, 10) # Add a random score penalty between 5-10 points
            break
        else:
            print("Invalid choice, please try again.")

def climb_the_mountain_range():
    global score
    print("You walk for what seems like hours, the scenery changing around you with every step.")
    time.sleep(2)
    print("The forest begins to thin out, and you can see the sun shining through the trees ahead.")
    time.sleep(2)
    print("As you emerge from the forest, you find yourself standing at the foot of a massive mountain range.")
    time.sleep(2)
    while True:
        choice = input("Will you (1) climb the mountain range or (2) circle around the mountain range? ")
        if choice == "1":
            print("No matter which option you choose, you eventually find yourself standing at the top of the mountain range, gazing out over the breathtaking vista below.")
            time.sleep(2)
            print("You feel a sense of accomplishment and satisfaction at having overcome the challenge before you.")
            score += random.randint(20, 30) # Add a random score bonus between 20-30 points
            break
        elif choice == "2":
            print("You circle around the mountain range, taking in the stunning views along the way.")
            score -= random.randint(5, 10) # Add a random score penalty between 5-10 points
            break
        else:
            print("Invalid choice, please try again.")

def visit_the_village():
    global score
    print("As you make your way down the other side of the mountain range, you come across a small village nestled in a valley.")
    time.sleep(2)
    while True:
        choice = input("Will you (1) stay in the village or (2) continue on your journey? ")
        if choice == "1":
            print("You spend a few days in the village, getting to know the friendly locals and enjoying their hospitality.")
            score += random.randint(30, 40) # Add a random score bonus between 30-40 points
        
        elif choice == "2":
            print("You bid farewell to the villagers and set out on the road once again, your heart filled with a sense of purpose and adventure.")
            score = random.randint(5, 10) # Add a random score penalty between 5-10 points
            
        else:
            print("Invalid choice, please try again.")

# Introduction
print("Welcome to The Path Ahead!")

# Player choices
score = 0
fork_in_the_road()
while True:
    choice = input("You suddenly come across asmall stream. Will you (1) follow the stream or (2) continue on the path? ")
    if choice == "1":
        follow_the_stream()
        break
    elif choice == "2":
        print("You continue on the path, the scenery around you changing with each step.")
        time.sleep(2)
        break
    else:
        print("Invalid choice, please try again.")

climb_the_mountain_range()

visit_the_village()

# Scoring consequences
if score >= 100:
    print("Congratulations! You completed the game with a high score!")
elif score >= 50:
    print("Well done! You completed the game with an average score.")
else:
    print("Sorry, you completed the game with a low score. Better luck next time!")

# Ask if the player wants to play again
while True:
    play_again = input("Would you like to play again? (Y/N): ")
    if play_again.upper() == "Y":
        print("Great! Let's play again.")
        score = 0 # Reset the score
        fork_in_the_road()
        while True:
            choice = input("You suddenly come across a small stream. Will you (1) follow the stream or (2) continue on the path? ")
            if choice == "1":
                follow_the_stream()
                break
            elif choice == "2":
                print("You continue on the path, the scenery around you changing with each step.")
                time.sleep(2)
                break
            else:
                print("Invalid choice, please try again.")

        climb_the_mountain_range()

        visit_the_village()

        if score >= 100:
            print("Congratulations! You completed the game with a high score!")
        elif score >= 50:
            print("Well done! You completed the game with an average score.")
        else:
            print("Sorry, you completed the game with a low score. Better luck next time!")
    elif play_again.upper() == "N":
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid choice, please try again.")
