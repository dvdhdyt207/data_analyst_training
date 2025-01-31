import numpy as np
import pandas as pd

df = pd.DataFrame({
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 
                       'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 
                   'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 
                       'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
    })

race = df['race'].value_counts()

avg_men = df[df['sex'] == 'Male']['age'].mean()

percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100
percentage_bachelors = round(percentage_bachelors, 1)

higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_rich = (higher_education['salary'] == '>50K' ).mean() * 100
higher_education_rich = round(higher_education_rich)

nothigher_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
nothigher_education_rich = (nothigher_education['salary'] == '>50K' ).mean() * 100
nothigher_education_rich = round(nothigher_education_rich)

min_works = df['hours-per-week'].min()

work_person = df[df['hours-per-week'] == 13]
min_works_person = (work_person['salary'] == '>50K').mean()
min_works_person = round(min_works_person)

cnt = df['native-country'].value_counts()

country_higher_income = df[df['salary'] == '>50K']

print(df)

#How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
print(race)

#What is the average age of men?
print(avg_men)

#What is the percentage of people who have a Bachelor's degree?
print(f"Percentage Bachelor's: {percentage_bachelors}%")

#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
print(f"Percentage's: {higher_education_rich}%")

#What percentage of people without advanced education make more than 50K?
print(f"Percentage's: {nothigher_education_rich}%")

#What is the minimum number of hours a person works per week?
print(min_works)

#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
print(f"Percentage's: {min_works_person}%")

#What country has the highest percentage of people that earn >50K and what is that percentage?
print(country_higher_income[['native-country', 'salary']])


#Identify the most popular occupation for those who earn >50K in India.
if df['native-country'].isin(['India']).any():
    print('India is in the data')
else:
    print('India is not in the data')