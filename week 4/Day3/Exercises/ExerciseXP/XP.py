# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


joined = dict(zip(keys, values))
print(joined)

# exercise 2
# Create a dictionary called store, and translate the information above into keys and values.
# Change the number of stores to 2.
# Print a sentence that explains who the competitors of Zara are.
# Add to the dictionary, a key called country_creation which value is Spain.
# If the key international_competitors is in the dictionary, add the store Desigual.
# Delete the information about the date of creation.
# Print the last international competitor.
# Print in a sentence, the major clothes’ colors in the US.
# Print the length of the dictionary.
# Print only the keys of the dictionary.
# Create another dictionary called more_on_zara with the following information:

# creation_date: 1975
# number_stores: 10 000

# Use a method to add the information from the dictionary more_on_zara to the dictionary store.
# Print the value of the key number_stores. What just happened ?


store = {'name': "Zara", 'creation_date': 1975, 'creator_name': ['Amancio' 'Ortega' 'Gaona'],
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'], 'number_stores': 2,
         'major_color': {'France': "blue", 'Spain': "red", 'US': ['pink', 'green']}}

print(store['number_stores'])

print(f'{store["name"]}\'s competitors are {store["international_competitors"]}')

store['country_creation'] = "Spain"
print(store['country_creation'])

if store['international_competitors']:
    store['international_competitors'].append('Desigual')
print(store['international_competitors'])

del store['creation_date']

print(store['international_competitors'][-1])

colours = store['major_color']['US']
print(f'The major clothes colors in the US are {colours[0]} and {colours[1]}')

print(len(store))

print(store.keys())

more_on_zara = {'creation_date': 1975,
                'number_stores': 10000}

store.update(more_on_zara)
print(store['number_stores'])

# Exercise 3
# Consider this list :
#
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# Analyse these results :
#
#1/ print(disney_users_A) >> {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/ print(disney_users_B) >> {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
# #3/ print(disney_users_C) >> {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# Use a for loop to recreate the #1 result. Tip : don’t hardcode the numbers
# Use a for loop to recreate the #2 result. Tip : don’t hardcode the numbers
# Use a method to recreate the #3 result
# Hint: The 3rd result is in the alphabetical order
# Recreate the #1 result, only if:
# The characters’ names contain the letter “i”.
# The characters’ names start with the letter “m” or “p”.

