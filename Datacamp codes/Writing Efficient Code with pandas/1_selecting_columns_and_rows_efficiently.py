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













