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


def prompt_user(df):
    while True:
        try:
            input_dog_breed = input("Please enter a dog breed: ").strip().lower()
            if input_dog_breed in df['Breed'].unique():
                dog_breed = input_dog_breed
                break
            else:
                raise KeyError
        except KeyError:
            print('Dog breed not found in the data. Please try again.\n')
    return dog_breed


def main():

    # Import data here
    df = pd.read_excel('CalgaryDogBreeds.xlsx', index_col=[0, 1])  # read xlsx file
    df['Breed'] = df['Breed'].str.lower()  # Convert dog breeds to lower case

    print("ENSF 692 Dogs of Calgary")

    # User input stage
    # dog_breed = prompt_user(df)
    dog_breed = 'beagle'

    print(dog_breed)
    print(df)
    # Data anaylsis stage

if __name__ == '__main__':
    main()
