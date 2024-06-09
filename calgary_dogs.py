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
            input_dog_breed = input("Please enter a dog breed: ").strip().upper()
            if input_dog_breed in df['Breed'].unique():
                dog_breed = input_dog_breed
                break
            else:
                raise KeyError
        except KeyError:
            print('Dog breed not found in the data. Please try again.\n')
    return dog_breed


def main():


    # Your code should include and use 
    # 3.05 at least one multi-index Pandas DataFrame, 
    # 3.05 at least one IndexSlice object, 
    # 3.02? at least one masking operation, 
    # 3.08? at least one grouping operation, 
    # 3.03? and at least one built-in Pandas or NumPy computational method.

    # Import data here
    df = pd.read_excel('CalgaryDogBreeds.xlsx', index_col=[])  # read xlsx file

    print("ENSF 692 Dogs of Calgary")

    # User input stage
    # dog_breed = prompt_user(df)
    dog_breed = 'LABRADOR RETR'
    
    # Add new calculated columns to deal with the data
    df['Percent'] = df['Total'] / np.sum(df['Total'])
    for year in (2021, 2022, 2023):
        df[f'{year} Percent'] = df['Total'][df['Year'] == year] / np.nansum(df['Total'][df['Year'] == year])

    # Data anaylsis stage

    # What years was the breed in the top breed?
    years_list = df[df['Breed'] == dog_breed]['Year'].unique()
    # we use a list comprehension to extract string versions of each year out of the array
    years_str = ' '.join([str(year) for year in years_list])
    print(f"The {dog_breed} was found in the top breeds for years: {years_str}")

    # How many were registered in total?
    print(f"There have been {np.sum(df[df['Breed'] == dog_breed]['Total'])} {dog_breed} dogs registered total.")

    # How popular in each year?
    for year in (2021, 2022, 2023):
        breed_this_year = 100 * np.nansum(df[df['Breed'] == dog_breed][f'{year} Percent'])
        print(f'The {dog_breed} was {breed_this_year:.6f}% of top breeds in {year}.')
    
    # and in all years?
    breed_all_years = 100 * np.sum(df.loc[df['Breed'] == dog_breed]['Percent'])
    print(f'The {dog_breed} was {breed_all_years:.6f}% of top breeds across all years.')



    print('_' * 50)




if __name__ == '__main__':
    main()
