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


def import_data():
    # read xlsx file
    file_path = 'CalgaryDogBreeds.xlsx'
    df = pd.read_excel(file_path)
    breeds = set(breed.lower() for breed in df['Breed'].unique())
    return df, breeds


def prompt_user(breeds):
    while True:
        try:
            input_dog_breed = input("Please enter a dog breed: ").strip().lower()
            if input_dog_breed in breeds:
                dog_breed = input_dog_breed
                break
            else:
                raise KeyError
        except KeyError:
            print('Dog breed not found in the data. Please try again.\n')
    return dog_breed


def main():

    # Import data here
    df, breeds = import_data()
    print(breeds)

    print("ENSF 692 Dogs of Calgary")

    # User input stage
    dog_breed = prompt_user(breeds)

    print(dog_breed)
    # Data anaylsis stage

if __name__ == '__main__':
    main()
