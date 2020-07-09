# Exercise 1
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
joined = dict(zip(keys, values))
print(joined)

# Exercise 2

# Here are some information about a store.

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: France -> blue, Spain -> red, US -> pink, green

# Create a dictionary called store, and translate the information above into keys and values.

# Change the number of stores to 2.

# Print a sentence that explains who the clients of Zara are.

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

# Bonus
#
# Add to the variable store, an empty dictionary called stores_worldwide.
# Outside of the dictionary, create a function addStore(country,number). This function checks if the key: stores_worldwide exists inside the dictionary store.
# If it does, then add to stores_worldwide, the arguments of the function as key and value.
# Print the value of the key stores_worldwide
# Add the method add_stores_worldwide to the variable store. Its value is the function created above.

store = {
    'name': "Zara",
    'creation_date': 1975,
    'creator_name': "Amancio Ortega Gaona",
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'number_stores': 7000,
    'major_color': France -> blue, Spain -> red, US -> pink, green
        }
