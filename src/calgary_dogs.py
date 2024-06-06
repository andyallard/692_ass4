# calgary_dogs.py
# Andy Allard
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd
import numpy as np


def prompt_user(breeds):
    """
    Prompt user for the school. User can enter either the school name or school code

    Arguments: breeds (dict): Dictionary of school codes and names
    Returns: 
        - school_code (int): school code for user's choice
        - school_name (str): school name for user's choice
    """
    while True:
        try:
            input_dog_breed = input("Please enter the high school name or"
                                      " school code: ").strip().lower()
            if input_dog_breed in breeds:  # check for the school code
                dog_breed = input_dog_breed
                break
            else:
                raise KeyError
        except KeyError:
            print('Dog breed not found in the data. Please try again.\n')
    return dog_breed


def main():

    # Import data here

    # read school names and codes from the .csv file and combine them into a dict named breeds
    file_path = '../specs/CalgaryDogBreeds.xlsx'
    df = pd.read_excel(file_path)
    print(df)
    breeds = df['Breed'].unique()
    print(breeds)

    print("ENSF 692 Dogs of Calgary")

    # User input stage

    # Data anaylsis stage

if __name__ == '__main__':
    main()
