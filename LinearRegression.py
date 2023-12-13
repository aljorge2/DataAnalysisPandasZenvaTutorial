#import pandas numpy matplotlib scipy.stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# read flights CSV file
flights = pd.read_csv("PythonZenva/DataAnalysisPANDAS/data-analysis/flights.csv", index_col = False)

# taking 1000 flights as subsample
flights_subsample = flights.sample(1000)

# plot the data showing relationship between how far away the airports are and time spent in the air
plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])
plt.show()

# perform linear regression distance of airports and time spent in air
slope, intercept, r_value, _, _ = linregress(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])
print('y = {}x + {}; r={}'.format(slope, intercept,r_value))

# numpy passing our min and max distances as range and picking a thousand values to fill out our line-of-best-fit:
x = np.linspace(flights_subsample['DISTANCE'].min(), flights_subsample['DISTANCE'].max(), 1000)

# computing y values for generated x values 
y = slope*x + intercept

# plot the data showing relationship between how far away the airports are and time spent in the air
plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])

# plotting line of best fit with scatterplot showing relationship between how far away the airports are and time spent in the air
plt.plot(x, y, 'r--')
plt.show()

# use learned slope and intercept for prediction
distance = 5000
flight_time = slope * distance + intercept
print(flight_time)