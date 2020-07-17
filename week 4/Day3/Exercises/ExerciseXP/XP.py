# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


joined = dict(zip(keys, values))
print(joined)

# exercise 2

store = {
    'name': "Zara",
    'creation_date': 1975,
    'creator_name': ['Amancio' 'Ortega' 'Gaona'],
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {'France': "blue", 'Spain': "red", 'US': ['pink', 'green']}
}


store['number_stores'] = 2
print(store['number_stores'])
print(f'{store["name"]}\'s competitors are {store["international_competitors"]}')
store['country_creation'] = "Spain"


if store['international_competitors']:
    store['international_competitors'].append('Desigual')

del store['creation_date']
print(store['international_competitors'])
