'''
Course: Writing Efficient Code with pandas

Chapter: 1 - Selecting columns and rows efficiently

This chapter will give you an overview of why efficient code matters and selecting specific and random rows and columns efficiently.

'''

'''
What does time.time() measure?
What does the time.time() function exactly measure?

-> The time since a predefined date and time set by the operating system.
The time.time() function shows the time (in seconds) since a pre-defined time, which in Unix-based systems is January 1, 1970.
'''

'''
Measure time I
'''

# Calculate the result of the problem using formula() and print the time required
N = 1000000
fm_start_time = time.time()
first_method = formula(N)
print("Time using formula: {} sec".format(time.time() - fm_start_time))

# Calculate the result of the problem using brute_force() and print the time required
sm_start_time = time.time()
second_method = brute_force(N)
print("Time using the brute force: {} sec".format(time.time() - sm_start_time))

#Time using formula: 9.322166442871094e-05 sec
#Time using the brute force: 0.08081889152526855 sec




'''
Measure time II
'''

# Store the time before the execution
start_time = time.time()

# Execute the operation
letlist = [wrd for wrd in words if wrd.startswith('b')]

# Store and print the difference between the start and the current time
total_time_lc = time.time() - start_time
print('Time using list comprehension: {} sec'.format(total_time_lc))
# Time using list comprehension: 0.046151161193847656 sec

# Store the time before the execution
start_time = time.time()

# Execute the operation
letlist = []
for wrd in words:
    if wrd.startswith('b'):
        letlist.append(wrd)
        
# Print the difference between the start and the current time
total_time_fl = time.time() - start_time
print('Time using for loop: {} sec'.format(total_time_fl))
# Time using for loop: 0.045410871505737305 sec




'''
Row selection: loc[] vs iloc[]
'''

# Define the range of rows to select: row_nums
row_nums = range(0, 1000)

# Select the rows using .loc[] and row_nums and record the time before and after
loc_start_time = time.time()
rows = poker_hands.loc[row_nums]
loc_end_time = time.time()

# Print the time it took to select the rows using .loc
print("Time using .loc[]: {} sec".format(loc_end_time - loc_start_time))

# Select the rows using .iloc[] and row_nums and record the time before and after
iloc_start_time = time.time()
rows = poker_hands.iloc[row_nums]
iloc_end_time = time.time()

# Print the time it took to select the rows using .iloc
print("Time using .iloc[]: {} sec".format(iloc_end_time - iloc_start_time))

# Time using .loc[]: 0.003068685531616211 sec
# Time using .iloc[]: 0.0014553070068359375 sec




'''
Column selection: .iloc[] vs by name
'''

# Use .iloc to select the first 6 columns and record the times before and after
iloc_start_time = time.time()
cols = poker_hands.iloc[:,0:6]
iloc_end_time = time.time()

# Print the time it took
print("Time using .iloc[] : {} sec".format(iloc_end_time - iloc_start_time))

# Use simple column selection to select the first 6 columns 
names_start_time = time.time()
cols = poker_hands[['S1', 'R1', 'S2', 'R2', 'S3', 'R3']]
names_end_time = time.time()

# Print the time it took
print("Time using selection by name : {} sec".format(names_end_time - names_start_time))

# Time using .iloc[] : 0.0010590553283691406 sec
# Time using selection by name : 0.0028002262115478516 sec




'''
Random row selection
'''

# Extract number of rows in dataset
N=poker_hands.shape[0]

# Select and time the selection of the 75% of the dataset's rows
rand_start_time = time.time()
poker_hands.iloc[np.random.randint(low=0, high=N, size=int(0.75 * N))]
print("Time using Numpy: {} sec".format(time.time() - rand_start_time))

# Select and time the selection of the 75% of the dataset's rows using sample()
samp_start_time = time.time()
poker_hands.sample(int(0.75 * N), axis=0, replace = True)
print("Time using .sample: {} sec".format(time.time() - samp_start_time))

# Time using Numpy: 0.003367185592651367 sec
# Time using .sample: 0.0023505687713623047 sec


'''
Random column selection
'''

# Extract number of columns in dataset
D=poker_hands.shape[1]

# Select and time the selection of 4 of the dataset's columns using NumPy
np_start_time = time.time()
poker_hands.iloc[:,np.random.randint(low=0, high=D, size=4)]
print("Time using NymPy's random.randint(): {} sec".format(time.time() - np_start_time))

# Select and time the selection of 4 of the dataset's columns using pandas
pd_start_time = time.time()
poker_hands.sample(4, axis=1)
print("Time using panda's .sample(): {} sec".format(time.time() - pd_start_time))

# 	Time using NymPy's random.randint(): 0.0029649734497070312 sec
# Time using panda's .sample(): 0.0016963481903076172 sec



