import random
import os


def put_a_car_behind_a_door(doors):
    return random.randint(1, doors)


def get_user_first_guess(doors):
    return random.randint(1, doors)


def is_guess_right(car, guess):
    return car == guess


def open_some_doors(car, guess, doors):
    goats = []
    if is_guess_right(car, guess):
        for i in range(1, doors + 1):
            if i != guess:
                goats.append(i)
        goats.remove(random.choice(goats))
        return goats
    else:
        for i in range(1, doors + 1):
            if i != guess and i != car:
                goats.append(i)
        return goats


def game_and_result(strategy, doors):
    car = put_a_car_behind_a_door(doors)
    guess = get_user_first_guess(doors)
    open_doors = open_some_doors(car, guess, doors)
    if strategy == 1:
        return guess == car
    for i in range(1, doors + 1):
        if i != guess and i not in open_doors:
            guess = i
            return guess == car


def show_results(strategy, repetitions, doors):
    os.system('clear')
    game_results = []
    while len(game_results) < repetitions:
        game_results.append(game_and_result(strategy, doors))
    print("With {} doors:".format(doors))
    if strategy == 1:
        print("When staying with the original door:")
    else:
        print("When switching to a new door:")
    print("\nCars:", sum(game_results))
    print("Goats:", repetitions - sum(game_results))


def get_strategy():
    while True:
        try:
            strategy = int(input('1: Stay\nor\n2: Switch\n'))
            if strategy in [1, 2]:
                return strategy
            print("That number wasn't an option.")
        except ValueError:
            print("Make sure you enter a number")


def get_repetitions():
    while True:
        try:
            repetitions = int(input('Run the simulation how many times? '))
            if repetitions > 0:
                return repetitions
            print("Make sure you enter a positive number")
        except ValueError:
            print("Make sure you enter a number")


def get_doors():
    while True:
        try:
            doors = int(input('How many doors? '))
            if doors >= 3:
                return doors
            print("There must be at least three doors.")
        except ValueError:
            print("Make sure you enter a number")


def main():
    while True:
        os.system('clear')
        strategy = get_strategy()
        repetitions = get_repetitions()
        doors = get_doors()
        show_results(strategy, repetitions, doors)
        if input("\nPlay again? ")[0].lower() == 'n':
            break

main()
