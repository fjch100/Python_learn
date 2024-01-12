# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fats because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia':'Moscow'}

# accessing the dictionary elements
print(capitals['Russia']) # Moscow
# using get() es safer
print(capitals.get('USA')) # Washington DC
print(capitals.get('Germany')) # None

# getting the keys as list
print(capitals.keys()) # ['USA', 'India', 'China', 'Russia']

# getting the values as list
print(capitals.values()) # ['Washington DC', 'New Dehli', 'Beijing', 'Moscow']

# printing all items
print(capitals.items()) # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

# looping the dictionary
for key, value in capitals.items():
    print(key, value) # USA Washington DC , India New Dehli, China Beijing, Russia Moscow

# changing the dictionary
capitals.update({'Germany':'Berlin'}) # adding one
capitals.update({'USA':'Las Vegas'})
print(capitals.items()) # dict_items([('USA', 'Las Vegas'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])

#removing one item
capitals.pop("China")

# clearing a dictionary
capitals.clear()
print()

