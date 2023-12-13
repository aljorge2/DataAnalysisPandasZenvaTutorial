# import PANDAS and numpy and matplotlib.pyplot
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# read flights CSV file
flights = pd.read_csv("PythonZenva/DataAnalysisPANDAS/data-analysis/flights.csv", index_col = False)

# load the mapping CSV file
days_of_week = pd.read_csv("PythonZenva/DataAnalysisPANDAS/data-analysis/L_WEEKDAYS.csv", index_col = False)

# the merge function allows us to pass our data set variables in any order and maps the columns according to the order specified. In the
#   example below the days of the week column in flights is associated to the code column in the days_of_week   

# merging flights data with days of the week data
merged = pd.merge(flights, days_of_week, left_on = "DAY_OF_WEEK", right_on = "Code")
print(merged)

# remove the DAY_OF_WEEK and Code columns (inplace=True)
merged.drop(columns=['DAY_OF_WEEK', 'Code'], inplace=True)

# rename Description -> DAY_OF_WEEK
merged.rename(columns={'Description': 'DAY_OF_WEEK'}, inplace=True)
print(merged)