import time
import random

def print_pause(message):
    print(message)
    time.sleep(2)

def fork_in_the_road(score):
    print_pause("\nYou find yourself standing at a fork in the road.")
    print_pause("To the left, the path appears to lead through a dense forest, while to the right, the path winds its way up a steep hill.")
    while True:
        choice = input(f"\nCurrent score: {score}. Which direction will you choose? (1) Go left or (2) Go right? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nNo matter which option you choose, you find yourself walking for what seems like hours.")
                print_pause("The forest grows thicker and darker.")
                score += random.randint(5, 15) # Add a random score bonus between 5-15 points
                print_pause(f"You earned {score} points!")
                break
            elif choice == 2:
                print_pause("\nNo matter which option you choose, you find yourself walking for what seems like hours.")
                print_pause("The hill becomes steeper and more treacherous.")
                score -= random.randint(5, 15) # Add a random score penalty between 5-15 points
                print_pause(f"You lost {score} points!")
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

    return score

def follow_the_stream(score):
    print_pause("\nNo matter which option you choose, you eventually come across a clearing in the woods.")
    print_pause("In the center of the clearing, you see a small, weather-beaten house.")
    while True:
        choice = input(f"\nCurrent score: {score}. Will you (1) approach the house or (2) stay in the clearing? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nNo matter which option you choose, you eventually find yourself standing in front of the house.")
                print_pause("You knock on the door, but no one answers.")
                score += random.randint(10, 20) # Add a random score bonus between 10-20 points
                print_pause(f"You earned {score} points!")
                break
            elif choice == 2:
                print_pause("\nYou stay in the clearing for a while, enjoying the peaceful surroundings.")
                score -= random.randint(5, 10) # Add a random score penalty between 5-10 points
                print_pause(f"You lost {score} points!")
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

    return score

def climb_the_mountain_range(score):
    print_pause("\nYou walk for what seems like hours, the scenery changing around you with every step.")
    print_pause("The forest begins to thin out, and you can see the sun shining through the trees ahead.")
    print_pause("As you emerge from the forest, you find yourself standing at the foot of a massive mountain range.")
    while True:
        choice = input(f"\nCurrent score: {score}. Will you (1) climb the mountain range or (2) circle around the mountain range? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nNo matter which option you choose, you eventually find yourself standing at the top of the mountain range, gazing out over the breathtaking vista below.")
                print_pause("You feel a sense of accomplishment and satisfaction at having overcome the challenge before you.")
                score += random.randint(20, 30) # Add a random score bonus between 20-30 points
                print_pause(f"You earned {score} points!")
                break
            elif choice == 2:
                print_pause("\nYou circle around the mountain range, taking in the stunning views along the way.")
                score -= random.randint(5, 10) # Add a random score penalty between 5-10 points
                print_pause(f"You lost {score} points!")
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

    return score

def visit_the_village(score):
    print_pause("\nAs you make your way down the other side of the mountain range, you come across a small village nestled in a valley.")
    while True:
        choice = input(f"\nCurrent score: {score}. Will you (1) stay in the village or (2)continue on your journey? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nYou spend some time in the village, enjoying the hospitality of the locals and learning about their way of life.")
                score += random.randint(10, 20) # Add a random score bonus between 10-20 points
                print_pause(f"You earned {score} points!")
                break
            elif choice == 2:
                print_pause("\nYou continue on your journey, eager to see what lies ahead.")
                score -= random.randint(5, 10) # Add a random score penalty between 5-10 points
                print_pause(f"You lost {score} points!")
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

    return score

def play_game():
    score = 0

    print_pause("Welcome to the adventure game!")
    print_pause("Your journey begins at the entrance to a dense forest.")
    print_pause("Your goal is to explore the world around you, make interesting choices, and earn as many points as possible.")

    score = fork_in_the_road(score)
    score = follow_the_stream(score)
    score = climb_the_mountain_range(score)
    score = visit_the_village(score)

    print_pause(f"\nGame over! Your final score is {score} points.")

play_game()
