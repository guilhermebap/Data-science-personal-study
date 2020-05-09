'''
Course: Working with Dates and Times in Python

Chapter 4: Easy and Powerful: Dates and Times in Pandas

To conclude this course, you'll apply everything you've learned 
about working with dates and times in standard Python to working 
with dates and times in Pandas. With additional information about 
each bike ride, such as what station it started and stopped at and 
whether or not the rider had a yearly membership, you'll be able to 
dig much more deeply into the bike trip data. In this chapter, you'll 
cover powerful Pandas operations, such as grouping and plotting 
results by time.

'''

import pandas as pd 
import numpy as np 


'''
Loading a csv file in Pandas
'''

# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv', 
                    parse_dates = ['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])




'''
Making timedelta columns
'''

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())




'''














