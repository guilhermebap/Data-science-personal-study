'''
Course: Working with Dates and Times in Python

Chapter: Dates and Calendars

Hurricanes (also known as cyclones or typhoons) hit the U.S. state 
of Florida several times per year. To start off this course, you'll 
learn how to work with date objects in Python, starting with the 
dates of every hurricane to hit Florida since 1950. You'll learn 
how Python handles dates, common date operations, and the right way 
to format dates to avoid confusion.

What was learned:
* datetime module
* time class
  Methods: strftime, isoformat, 
* timedelta class

'''



import numpy as np 
import pandas as pd 

# Import date from datetime
from datetime import date

'''
Which day of the week?
'''

# Create a date object
hurricane_andrew = date(1992, 8, 24)

# Which day of the week is the date?
print(hurricane_andrew.weekday())



'''
How many hurricanes come early?
'''

# Counter for how many before June 1
early_hurricanes = 0

# We loop over the dates
for hurricane in florida_hurricane_dates:
  # Check if the month is before June (month number 6)
  if hurricane.month < 6:
    early_hurricanes = early_hurricanes + 1
    
print(early_hurricanes)



'''
Subtracting dates
'''

# Import date
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)



'''
Counting events per calendar month
'''

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1
  
print(hurricanes_each_month)



'''
Putting a list of dates in order
'''

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])



'''
Printing dates in a friendly format
'''

# Assign the earliest date to first_date
first_date = florida_hurricane_dates[0]

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)



'''
Representing dates in different ways
'''

# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)'))

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j'))





