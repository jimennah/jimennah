import random
import time


def print_pause(message):
    print(message)
    time.sleep(2)


def fork_in_the_road(score):
    print_pause("\nYou find yourself at a fork in the road.")
    while True:
        choice = input(f"\nCurrent score: {score}. Will you (1) take the left "
                       f"path or (2) take the right path? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nYou take the left path and continue on your "
                            "journey.")
                break
            elif choice == 2:
                print_pause("\nYou take the right path and find yourself at "
                            "the edge of a stream.")
                score -= random.randint(5, 10)  # Add a random score penalty
                print_pause(f"You lost {score} points!")
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

    return score


def follow_the_stream(score):
    print_pause("\nYou follow the stream and come across a waterfall.")
    while True:
        choice = input(f"\nCurrent score: {score}. Will you (1) climb the "
                       f"waterfall or (2) continue downstream? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nYou climb the waterfall and reach the top.")
                score += random.randint(10, 20)  # Add a random score bonus
                print_pause(f"You earned {score} points!")
                break
            elif choice == 2:
                print_pause("\nYou continue downstream and eventually come "
                            "to a clearing.")
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

    return score


def climb_the_mountain_range(score):
    print_pause("\nYou come across a mountain range and decide to climb it.")
    while True:
        choice = input(f"\nCurrent score: {score}. Will you (1) climb the "
                       f"steep cliffs or (2) take the longer, safer route? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nYou start climbing the steep cliffs and reach "
                            "the top.")
                score += random.randint(10, 20)  # Add a random score bonus
                print_pause(f"You earned {score} points!")
                break
            elif choice == 2:
                print_pause("\nYou take the longer, safer route and eventually"
                            "reach the top of the mountain range, taking in "
                            "the stunning views along the way.")
                score -= random.randint(5, 10)  # Add a random score penalty
                print_pause(f"You lost {score} points!")
                break
            else:
                print_pause("Invalid choice, please try again.")
        else:
            print_pause("Invalid input, please enter a number (1 or 2).")

    return score


def visit_the_village(score):
    print_pause("\nAs you make your way down the other side of the mountain "
                "range, you come across a small village nestled in a valley.")
    while True:
        choice = input(f"\nCurrent score: {score}. Will you (1) stay in the "
                       f"village or (2) continue on your journey? ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print_pause("\nYou spend some time in the village, enjoying "
                            "the hospitality of the locals and learning about "
                            "their way of life.")
                score += random.randint(10, 20)  # Add a random score bonus
                print_pause(f"You earned {score} points!")
                break
            elif choice == 2:
                print_pause("\nYou continue on your journey, eager to see "
                            "what lies ahead.")
                score -= random.randint(5, 10)  # Add a random score penalty
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
    print_pause("Your goal is to explore the world around you, make "
                "interesting choices, and earn as many points as possible.")

    score = fork_in_the_road(score)
    score = follow_the_stream(score)
    score = climb_the_mountain_range(score)
    score = visit_the_village(score)

    print_pause(f"\nGame over! Your final score is {score} points.")


play_game()
# Add a blank line at the end of the file
