import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# read flights CSV file
flights = pd.read_csv("PythonZenva/DataAnalysisPANDAS/data-analysis/flights.csv", index_col = False)

# printing basic statistics of flight data
print(flights.describe())

# note that the basic statistical results are applied to every column and some do not make sense such as the year column

print(flights['DISTANCE'].mean())
print(flights['DISTANCE'].std())
# The resulting mean for the DISTANCE column is 855.988945, exactly as in the table above. 
#   The same happens to its deviation: 623.7331269256721.

# mean of the difference of CRS departure and actual departure times
print((flights['CRS_DEP_TIME'] - flights['DEP_TIME']).mean())

# the negative value indicates that we can expect flights to be a little late