import random
import os


def put_a_car_behind_a_door():
    return random.randint(1, 3)


def get_user_first_guess():
    return random.randint(1, 3)


def is_guess_right(car, guess):
    return car == guess


def open_one_door(car, guess):
    if is_guess_right(car, guess):
        goats = []
        for i in range(1, 4):
            if i != guess:
                goats.append(i)
        return random.choice(goats)
    else:
        for i in range(1, 4):
            if i != guess and i != car:
                return i


def game_and_result(strategy):
    car = put_a_car_behind_a_door()
    guess = get_user_first_guess()
    open_door = open_one_door(car, guess)
    if strategy == 1:
        return guess == car
    for i in range(1, 4):
        if i != guess and i != open_door:
            guess = i
            return guess == car


def show_results(strategy, repetitions):
    os.system('clear')
    game_results = []
    while len(game_results) < repetitions:
        game_results.append(game_and_result(strategy))
    if strategy == 1:
        print("When staying with the original door:\n")
    else:
        print("When switching to a new door:\n")
    print("Cars:", sum(game_results))
    print("Goats:", repetitions - sum(game_results))


def main():
    os.system('clear')
    strategy = int(input('1: Stay\nor\n2: Switch\n'))
    repetitions = int(input('Run the simulation how many times? '))
    show_results(strategy, repetitions)


main()
