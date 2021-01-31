countries = [
    {
        'country': 'South Africa',
        'capital': 'Pretoria',
        'continent': 'Africa'
    },
    {
        'country': 'USA',
        'capital': 'Washington DC',
        'continent': 'North America'
    },
    {
        'country': 'Panama',
        'capital': 'Panama City',
        'continent': 'North America'
    },
    {
        'country': 'Israel',
        'capital': 'Jerusalem',
        'continent': 'Asia'
    },
    {
        'country': 'Palestine',
        'capital': 'Al Quds',
        'continent': 'Asia'
    }
]

continents = set()
for country in countries:
    continents.add(country['continent'])

names = ["jon", "omri", "jason"]

capitol = {name[0].upper(): name for name in names}

phonebook = {}

for name in names:
    key = name[0].upper()

    if key not in phonebook:
        phonebook[key] = [name]
    else:
        phonebook[key].append(name)

print(phonebook)
