'''
Course: Writing Efficient Python Code

Chapter: 2 - Timing and profiling code

In this chapter, you will learn how to gather and compare runtimes 
between different coding approaches. You'll practice using the line_profiler 
and memory_profiler packages to profile your code base and spot bottlenecks. 
Then, you'll put your learnings to practice by replacing these bottlenecks 
with efficient Python code.
'''

'''
Using %timeit: your turn!
'''

%timeit nums_list_comp = [num for num in range(51)]
# 2.89 us +- 371 ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)

%timeit nums_unpack = [*range(51)]
# 469 ns +- 8.51 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)





'''
Using %timeit: specifying number of runs and loops

%timeit lets you specify the number of runs and number of loops you want 
to consider with the -r and -n flags. You can use -r5 and -n25 to specify 
5 iterations each with 25 loops when calculating the average and standard 
deviation of runtime for your code.
'''

%timeit -r5 -n25 set(heroes)
# 19.3 us +- 2.36 us per loop (mean +- std. dev. of 5 runs, 25 loops each)




'''
Using %timeit: formal name or literal syntax
'''

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))


%timeit formal_list = list()
# 78.6 ns +- 3.33 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit literal_list = []
# 19.9 ns +- 0.501 ns per loop (mean +- std. dev. of 7 runs, 100000000 loops each)





'''
Using cell magic mode (%%timeit)

You used %%timeit (cell magic mode) to time multiple lines of code. Converting the 
wts list into a NumPy array and taking advantage of NumPy array broadcasting saved 
you some time! Moving forward, remember that you can use %timeit to gather runtime 
for a single line of code (line magic mode) and %%timeit to get the runtime for 
multiple lines of code.
'''

%%timeit 
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)
# 860 us +- 46.1 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

%%timeit
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462
# 14.9 us +- 1.03 us per loop (mean +- std. dev. of 7 runs, 100000 loops each)



'''
Using %lprun: spot bottlenecks
'''

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data


%load_ext line_profiler
%lprun -f convert_units convert_units(heroes, hts, wts)

'''
Timer unit: 1e-06 s

Total time: 0.000928 s
File: <ipython-input-1-2ae8c0194a47>
Function: convert_units at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units(heroes, heights, weights):
     2                                           
     3         1        124.0    124.0     13.4      new_hts = [ht * 0.39370  for ht in heights]
     4         1        150.0    150.0     16.2      new_wts = [wt * 2.20462  for wt in weights]
     5                                           
     6         1          1.0      1.0      0.1      hero_data = {}
     7                                           
     8       481        316.0      0.7     34.1      for i,hero in enumerate(heroes):
     9       480        336.0      0.7     36.2          hero_data[hero] = (new_hts[i], new_wts[i])
    10                                                   
    11         1          1.0      1.0      0.1      return hero_data
'''




'''
Using %lprun: fix the bottleneck
'''

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

%load_ext line_profiler
%lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

'''
Timer unit: 1e-06 s

Total time: 0.00058 s
File: <ipython-input-3-84e44a6b12f5>
Function: convert_units_broadcast at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units_broadcast(heroes, heights, weights):
     2                                           
     3                                               # Array broadcasting instead of list comprehension
     4         1         23.0     23.0      4.0      new_hts = heights * 0.39370
     5         1          4.0      4.0      0.7      new_wts = weights * 2.20462
     6                                           
     7         1          1.0      1.0      0.2      hero_data = {}
     8                                           
     9       481        241.0      0.5     41.6      for i,hero in enumerate(heroes):
    10       480        311.0      0.6     53.6          hero_data[hero] = (new_hts[i], new_wts[i])
    11                                                   
    12         1          0.0      0.0      0.0      return hero_data
'''




'''
Pop quiz: steps for using %mprun

 - Use the command from hero_funcs import convert_units to load the function you'd like to profile.

 - Use %load_ext memory_profiler to load the memory_profiler within your IPython session.

 - Use %mprun -f convert_units convert_units(heroes, hts, wts) to get line-by-line memory allocations.

Remember that using %mprun requires one additional step compared to using %lprun (i.e., you need to 
import the function in order to use %mprun on it). Now that you've reviewed these necessary steps, 
practice profiling for memory usage!
'''

'''
Using %mprun: Hero BMI
'''

def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis

from bmi_lists import calc_bmi_lists

%load_ext memory_profiler 

%mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)

'''
Filename: /tmp/tmpujkx1mek/bmi_lists.py

Line #    Mem usage    Increment   Line Contents
================================================
     1    109.0 MiB    109.0 MiB   def calc_bmi_lists(sample_indices, hts, wts):
     2                             
     3                                 # Gather sample heights and weights as lists
     4    109.0 MiB      0.0 MiB       s_hts = [hts[i] for i in sample_indices]
     5    109.0 MiB      0.0 MiB       s_wts = [wts[i] for i in sample_indices]
     6                             
     7                                 # Convert heights from cm to m and square with list comprehension
     8    109.0 MiB      0.0 MiB       s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]
     9                             
    10                                 # Calculate BMIs as a list with list comprehension
    11    109.0 MiB      0.0 MiB       bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]
    12                             
    13    109.0 MiB      0.0 MiB       return bmis
'''
'''
Using a list comprehension approach allocates anywhere from 0.1 MiB to 2 MiB of memory to calculate your BMIs.

If you run %mprun multiple times within your session, you may notice that the Increment column reports 
0.0 MiB for all lines of code. This is due to a limitation with the magic command. After running %mprun 
once, the memory allocation analyzed previously is taken into account for all consecutive runs and %mprun 
will start from the place the first run left off.
'''




'''
Using %mprun: Hero BMI 2.0
'''

def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis

from bmi_arrays import calc_bmi_arrays

%load_ext memory_profiler

%mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices, hts, wts)

'''
Filename: /tmp/tmpujkx1mek/bmi_arrays.py

Line #    Mem usage    Increment   Line Contents
================================================
     1    109.3 MiB    109.3 MiB   def calc_bmi_arrays(sample_indices, hts, wts):
     2                             
     3                                 # Gather sample heights and weights as arrays
     4    109.3 MiB      0.0 MiB       s_hts = hts[sample_indices]
     5    109.3 MiB      0.0 MiB       s_wts = wts[sample_indices]
     6                             
     7                                 # Convert heights from cm to m and square with broadcasting
     8    109.5 MiB      0.1 MiB       s_hts_m_sqr = (s_hts / 100) ** 2
     9                             
    10                                 # Calculate BMIs as an array using broadcasting
    11    109.5 MiB      0.0 MiB       bmis = s_wts / s_hts_m_sqr
    12                             
    13    109.5 MiB      0.0 MiB       return bmis
'''




'''
Bringing it all together: Star Wars profiling
'''

def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes

def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes


# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

%load_ext line_profiler

%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')
'''
Timer unit: 1e-06 s

Total time: 0.000297 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2                                           
     3         1          2.0      2.0      0.7      desired_heroes = []
     4                                           
     5       481        150.0      0.3     50.5      for i,pub in enumerate(publishers):
     6       480        132.0      0.3     44.4          if pub == desired_publisher:
     7         4         12.0      3.0      4.0              desired_heroes.append(heroes[i])
     8                                           
     9         1          1.0      1.0      0.3      return desired_heroes
'''

%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')
'''
Timer unit: 1e-06 s

Total time: 0.000203 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes_np at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    13                                           
    14         1        141.0    141.0     69.5      heroes_np = np.array(heroes)
    15         1         44.0     44.0     21.7      pubs_np = np.array(publishers)
    16                                           
    17         1         18.0     18.0      8.9      desired_heroes = heroes_np[pubs_np == desired_publisher]
    18                                           
    19         1          0.0      0.0      0.0      return desired_heroes
'''

%load_ext memory_profiler

from hero_funcs import get_publisher_heroes
from hero_funcs import get_publisher_heroes_np

%mprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')

%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes, publishers, 'George Lucas')

