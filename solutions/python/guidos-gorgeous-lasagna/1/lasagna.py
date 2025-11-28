"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#Define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 100
PREP_TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers = 1):
    """Calculate the total preparation time.

    :param number_of_layers: int - number of layers.
    :return: int - total bake time (in minutes) derived from 'PREP_TIME_PER_LAYER'.

    Function that takes the numbers of layers in the lasagna and returns how many minutes it 
    takes to prepare that number of layers `PREP_TIME_PER_LAYER`.
    """
    return number_of_layers * PREP_TIME_PER_LAYER


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): 
    """Calculate the elapsed time making the lasagna.

    :param number_of_layers: int - number of layers.
    :return: int - time (in minutes) spent preparing the lasagna.

    Function that takes the numbers of layers in the lasagna and the elapsed_bake_time and         returns how many minutes it have already been spent preparing the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

