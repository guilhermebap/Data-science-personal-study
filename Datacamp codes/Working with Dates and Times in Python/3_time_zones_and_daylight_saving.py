'''
Course: Working with Dates and Times in Python

Chapter: Time Zones and Daylight Saving

In this chapter, you'll learn to confidently tackle the time-related 
topic that causes people the most trouble: time zones and daylight 
saving. Continuing with our bike data, you'll learn how to compare 
clocks around the world, how to gracefully handle "spring forward" 
and "fall back," and how to get up-to-date timezone data from the 
dateutil library.

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











