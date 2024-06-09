# calgary_dogs.py
# Andy Allard
#
# A terminal-based application for computing and printing statistics based on given input.

import pandas as pd
import numpy as np


def main():
    # Import data here
    df = pd.read_excel('CalgaryDogBreeds.xlsx', index_col=[])  # read xlsx file

    print("ENSF 692 Dogs of Calgary")

    # User input stage
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
    
    # Add new calculated columns to deal with the data
    df['Percent'] = df['Total'] / np.sum(df['Total'])
    # Here we use a BUILT-IN NUMPY COMPUTATIONAL METHOD, np.nansum()
    for year in (2021, 2022, 2023):
        df[f'{year} Percent'] = df['Total'][df['Year'] == year] / np.nansum(df['Total'][df['Year'] == year], axis=0)

    # Data anaylsis stage

    # What years was the breed in the top breed? 
    # We use a MASKING OPERATION
    years_list = df[df['Breed'] == dog_breed]['Year'].unique()
    # we use a list comprehension to extract string versions of each year out of the array
    years_str = ' '.join([str(year) for year in years_list])
    print(f"The {dog_breed} was found in the top breeds for years: {years_str}")

    # How many were registered in total?
    # We use a GROUPING OPERATION
    print(f"There have been {df.groupby('Breed')['Total'].sum()[dog_breed]} {dog_breed} dogs registered total.")

    # How popular in each year?
    for year in (2021, 2022, 2023):
        breed_this_year = 100 * np.nansum(df[df['Breed'] == dog_breed][f'{year} Percent'])
        print(f'The {dog_breed} was {breed_this_year:.6f}% of top breeds in {year}.')
    # and in all years?
    breed_all_years = 100 * np.sum(df.loc[df['Breed'] == dog_breed]['Percent'])
    print(f'The {dog_breed} was {breed_all_years:.6f}% of top breeds across all years.')

    # Most popular months
    # First we create a MULTI-INDEX PANDAS DATAFRAME
    df_multi = df.set_index(['Breed', 'Year', 'Month'])
    # We'll now extract data on user's breed using an INDEXSLICE OBJECT
    idx = pd.IndexSlice
    breed_info = df_multi.loc[idx[dog_breed, :, :]]
    # Find most times the breed was registered in a month using a GROUPING OPERATION
    most_months = breed_info.groupby(['Month'])['Total'].count().max()
    # Now we use a MASKING OPERATION to determine which months tied for most registrations
    popular_month_mask = breed_info.groupby(['Month'])['Total'].count() == most_months
    # Now we convert the list of months (stored in the resulting index) into a string
    popular_months = ' '.join([str(month) for month in popular_month_mask[popular_month_mask].index])
    # And display to console
    print(f'Most popular month(s) for {dog_breed} dogs: {popular_months}')

if __name__ == '__main__':
    main()
