# import PANDAS and numpy
import pandas as pd 
import numpy as np

# read flights CSV file
flights = pd.read_csv("PythonZenva/DataAnalysisPANDAS/data-analysis/flights.csv", index_col = False)

# printing data types of all columns
print(flights.dtypes)

# checking to see if each column is the most suitable data type possible. he term object in the second
#   column of flights.dtype actually refers to strings. The column FL_DATE which houses the date of the
#   flight is a string. It would be best if it were of a date/type type. To convert the the 

#changing flight data to date/time datatype
flights['FL_DATE'] = pd.to_datetime(flights['FL_DATE'])
print(flights.dtypes)

# Changing cancelled and diverted to boolean values as indicated in README
flights['CANCELLED'] = flights['CANCELLED'].astype(bool)
flights['DIVERTED'] = flights['DIVERTED'].astype(bool)
print(flights.dtypes)

# we see that we have columns for YEAR, MONTH and DAY_OF_MONTH, besides our already converted FL_DATE. We do not need all those extra
#    columns. We could either keep the first three columns or the last one (as the latter already encapsulates the three others). If 
#    each of the date information columns will be analyzed separately, we should keep them and discard the FL_DATE one. Otherwise, we 
#    could just save space and look at the FL_DATE directly (thus, deleting the other three date-related columns). 

# to remove columns we do the following 

# remove columns YEAR, MONTH, DAY_OF_MONTH
flights.drop(columns=['YEAR', 'MONTH', 'DAY_OF_MONTH'],inplace=True) 

# the “inplace=True” is simply indicating that our “flights” DataFrame columns will be modified directly

# to rename a column we do the following 

# rename columns
flights.rename(columns={'DEST': 'DESTINATION'},inplace=True)

# the above command passes a dictionary to nape the old name to new ones

# we can get the number of null/missing values for each category using the following 

# fetching number of null values
print(flights.isnull().sum())

# Pandas is good at handling missing values as it will do something called null propagation. Meaning if in a sum one of the numbers is
#    null the result of any operation involving the value will also be null. "dropna()" can remove null values from a dataset In Pandas
#    documentation, you can find an entire section on how to deal with missing data and data cleaning in general (to see more go to : 
#    http://pandas.pydata.org/pandas-docs/stable/). 
