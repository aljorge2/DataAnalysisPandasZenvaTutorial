# import PANDAS and numpy and matplotlib.pyplot
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# read flights CSV file
flights = pd.read_csv("PythonZenva/DataAnalysisPANDAS/data-analysis/flights.csv", index_col = False)

# to plot a histogram you do the following 

# plot a histogram of CRS departure times
histogram = flights['CRS_DEP_TIME'].hist()
plt.show()

# plot a histogram of CRS arrival times
flights['CRS_ARR_TIME'].hist()
plt.show()

# plot average distance that flights travel by month
flights_by_month = flights.groupby('MONTH')
flights_by_month['DISTANCE'].aggregate(np.mean).plot()
plt.show()

#plot average distance that flights travel by day of the week
flights_by_week = flights.groupby("DAY_OF_WEEK")
flights_by_week["DISTANCE"].aggregate(np.mean).plot()
plt.show()