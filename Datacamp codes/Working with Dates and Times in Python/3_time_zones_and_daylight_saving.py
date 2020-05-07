'''
Course: Working with Dates and Times in Python

Chapter: Time Zones and Daylight Saving

In this chapter, you'll learn to confidently tackle the time-related 
topic that causes people the most trouble: time zones and daylight 
saving. Continuing with our bike data, you'll learn how to compare 
clocks around the world, how to gracefully handle "spring forward" 
and "fall back," and how to get up-to-date timezone data from the 
dateutil library.

What was learned:
* timezone class from datetime package
    method: astimezone
    how to create a timezone
    et = timezone(timedelta(hours=-5))

* tz class from dateutil package - package used for get timezone information
    method: et = gettz('Continent/City')
            datetime_ambiguous
            enfold

* How to set the timezone to a datetime object - tzinfo or replace method from datetime

* To make comparisons between dates, switch into utc


'''

import pandas as pd 
import numpy as np 


'''
Creating timezone aware datetimes
'''

# Import datetime, timezone
from datetime import datetime, timezone

# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat())

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())

# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours=+11))

# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)

# Print results
print(dt.isoformat())




'''
Setting timezones
'''

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=edt)
  trip['end'] = trip['end'].replace(tzinfo=edt)




'''
What time did the bike leave in UTC?
'''

# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start and set it to UTC
  dt = trip['start'].astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())




'''
Putting the bike trips into the right time zone
'''

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
  # Update trip['start'] and trip['end']
  trip['start'] = trip['start'].replace(tzinfo=et)
  trip['end'] = trip['end'].replace(tzinfo=et)




'''
What time did the bike leave? (Global edition)

When you need to move a datetime from one timezone into another, 
use .astimezone() and tz. Often you will be moving things into UTC, 
but for fun let's try moving things from 'America/New_York' into a 
few different time zones.
'''

# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in India?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())




'''
How many hours elapsed around daylight saving?
'''
# Import datetime, timedelta, tz, timezone
from datetime import datetime, timedelta, timezone
from dateutil import tz

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# What if we move to UTC?
print((end.astimezone(timezone.utc) - start.astimezone(timezone.utc))\
      .total_seconds()/(60*60))




'''
March 29, throughout a decade

Daylight Saving rules are complicated: they're different in different 
places, they change over time, and they usually start on a Sunday 
(and so they move around the calendar).

For example, in the United Kingdom, as of the time this lesson was 
written, Daylight Saving begins on the last Sunday in March. Let's 
look at the UTC offset for March 29, at midnight, for the years 
2000 to 2010.

When in doubt, always use tz instead of hand-rolling timezones, so 
it will catch the Daylight Saving rules (and rule changes!) for you.
'''

# Import datetime and tz
from datetime import datetime
from dateutil import tz

# Create starting date
dt = datetime(2000, 3, 29, tzinfo = tz.gettz('Europe/London'))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year=y).isoformat())





'''
Finding ambiguous datetimes
'''

# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end 
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))




'''
Cleaning daylight saving data with fold

Since Python does not handle tz.enfold() when doing arithmetic, 
we must put our datetime objects into UTC, where ambiguities have been resolved.
'''

trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip['start'] > trip['end']:
    trip['end'] = tz.enfold(trip['end'])
  # Convert to UTC
  start = trip['start'].astimezone(tz.UTC)
  end = trip['end'].astimezone(tz.UTC)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))

'''
Good work! Now you know how to handle some pretty gnarly edge cases in 
datetime data. To give a sense for how tricky these things are: we actually 
still don't know how long the rides are which only started or ended in our 
ambiguous hour but not both. If you're collecting data, store it in UTC or 
with a fixed UTC offset!
'''





