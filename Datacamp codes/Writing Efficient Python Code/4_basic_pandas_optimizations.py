'''
Course: Writing Efficient Python Code

Chapter: 4 - Basic pandas optimizations

This chapter offers a brief introduction on how to efficiently work with 
pandas DataFrames. You'll learn the various options you have for iterating 
over a DataFrame. Then, you'll learn how to efficiently apply functions to 
data stored in a DataFrame.
'''

'''
Iterating with .iterrows()

.iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs.
'''

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(type(row))
    print(row)
    
# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

'''
Nice work! Since .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) 
pairs, you can either split this tuple and use the index and row-values separately 
(as you did with for i,row in pit_df.iterrows()), or you can keep the result of .iterrows() 
in the tuple form (as you did with for row_tuple in pit_df.iterrows()).

If using i,row, you can access things from the row using square brackets (i.e., row['Team']). 
If using row_tuple, you would have to specify which element of the tuple you'd like to access 
before grabbing the team name (i.e., row_tuple[1]['Team']).

With either approach, using .iterrows() will still be substantially faster than using .iloc 
as you saw in the video.
'''



'''
Run differentials with .iterrows()
'''

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)




'''
Iterating with .itertuples()

Remember, .itertuples() returns each DataFrame row as a special data 
type called a namedtuple. You can look up an attribute within a namedtuple 
with a special syntax

You need to use the dot syntax for referencing an attribute in a namedtuple
'''

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)




'''
Run differentials with .itertuples()
'''

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)




'''
Analyzing baseball stats with .apply()

The .apply() method let's you apply functions to all rows or columns of a DataFrame by specifying an axis.
You could have used rays_df.sum(axis=0) to get columnar sums and rays_df[['RS', 'RA']].sum(axis=1) to get row sums.

You could have also used .apply() directly on a Series (or column) of the DataFrame. For example, you could use 
rays_df['Playoffs'].apply(text_playoffs) to convert the 'Playoffs' column to text.
'''

def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)





'''
Settle a debate with .apply()

Nicely done! Using the .apply() method with a lambda function allows you to apply a function to a DataFrame 
without the need to write a for loop.	
'''

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)


# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])





'''
Replacing .iloc with underlying arrays
'''

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list


# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

%%timeit
win_percs_list = []
for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]
    wins = row['W']
    games_played = row['G']
    win_perc = calc_win_perc(wins, games_played)
    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list

# 1.39 s +- 36.9 ms per loop (mean +- std. dev. of 7 runs, 1 loop each)

%%timeit
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)
baseball_df['WP'] = win_percs_np

# 618 us +- 54.5 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)




'''
Bringing it all together: Predict win percentage
'''

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)


win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)


# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)


# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

%%timeit
win_perc_preds_loop = []
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)
#42.2 ms +- 4.15 ms per loop (mean +- std. dev. of 7 runs, 10 loops each)

%timeit win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)
# 190 ms +- 15 ms per loop (mean +- std. dev. of 7 runs, 1 loop each)

%timeit win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
# 69.9 us +- 2.35 us per loop (mean +- std. dev. of 7 runs, 10000 loops each)












