'''
Course: Writing Efficient Python Code

Chapter: 3 - Gaining efficiencies

This chapter covers more complex efficiency tips and tricks. You'll learn a 
few useful built-in modules for writing efficient code and practice using 
set theory. You'll then learn about looping patterns in Python and how to 
make them more efficient.
'''

'''
Combining Pokémon names and types
'''

# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')




'''
Counting Pokémon from a sample
'''

from collections import Counter

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [i[0] for i in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)




'''
Combinations of Pokémon
'''

# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)




'''
Comparing Pokédexes
'''
ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)




'''
Searching for Pokémon
'''

brock_pokedex = ['Onix', 'Geodude', 'Zubat', 'Golem', 'Vulpix', 'Tauros', 'Kabutops', 'Omastar', 'Machop', 'Dugtrio']
# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

%timeit 'Psyduck' in ash_pokedex
# 129 ns +- 1.91 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit 'Psyduck' in brock_pokedex_set
# 28.6 ns +- 0.976 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit 'Machop' in ash_pokedex
# 134 ns +- 5.81 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit 'Machop' in brock_pokedex_set
# 27.5 ns +- 0.282 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)




'''
Gathering unique Pokémon
'''








