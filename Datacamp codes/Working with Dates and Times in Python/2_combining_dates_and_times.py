'''
Course: Working with Dates and Times in Python

Chapter: Combining Dates and Times

Bike sharing programs have swept through cities around the 
world -- and luckily for us, every trip gets recorded! Working 
with all of the comings and goings of one bike in Washington, 
D.C., you'll practice working with dates and times together. 
You'll parse dates and times from text, analyze peak trip times, 
calculate ride durations, and more.

'''

import numpy as np 
import pandas as pd 

'''
Creating datetimes by hand
'''

# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print(dt.isoformat())

# Replace the year with 1917
dt_old = dt.replace(year=1917)

# Print the results in ISO 8601 format
print(dt_old)



'''
Counting events before and after noon
'''

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}
  
# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1
  
print(trip_counts)



'''
Turning strings into datetimes

Reference	
%Y	4 digit year (0000-9999)
%m	2 digit month (1-12)
%d	2 digit day (1-31)
%H	2 digit hour (0-23)
%M	2 digit minute (0-59)
%S	2 digit second (0-59)
'''

# Import the datetime class
from datetime import datetime

# Starting string, in YYYY-MM-DD HH:MM:SS format
s = '2017-02-03 00:00:01'

# Write a format string to parse s
fmt = '%Y-%m-%d %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)

# Starting string, in YYYY-MM-DD format
s = '2030-10-15'

# Write a format string to parse s
fmt = '%Y-%m-%d'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)

# Starting string, in MM/DD/YYYY HH:MM:SS format
s = '12/15/1986 08:00:00'

# Write a format string to parse s
fmt = '%m/%d/%Y %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)



'''
Parsing pairs of strings as datetimes
'''

