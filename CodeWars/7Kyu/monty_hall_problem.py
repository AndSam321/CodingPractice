'''Checking if the correct_door is not the correct guess then switch. Count the number of switches
and then divide by the amount of guesses.

'''
import math
def monty_hall(correct_door_number, participant_guesses):
    switch_number = 0
    length_of_guesses = len(participant_guesses)
    for guess in participant_guesses:
        if guess != correct_door_number:
            switch_number = switch_number + 1
    answer = round((switch_number/length_of_guesses) * 100)
    return answer