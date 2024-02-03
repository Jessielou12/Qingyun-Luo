# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of state and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
} 

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ",cities['NY'])
print("OR State has: ",cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is :", states['Michigan'])
print("Florida's abbreviation is :", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ",cities[states['Michigan']])   # Dictionaries can be indexed by variables
print("Florida has: ",cities[states['Florida']])
 
# print every state abbreviation
print('-' * 10) 
for state, abbrev in states.items():    # The two variables are assigned as keys and values in the states dictionary
    print("%s is abbreviated %s" % (state, abbrev))
    
# print every city in state
print('-' * 10) 
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev,city))
 
# now do both at the same time
print('-' * 10) 
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]))
        
print('-' * 10) 
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)     # The get() function returns the value of the specified key, or the default value if the value is not in the dictionary.
if not state:    # This is to determine whether state has a value
    print("Sorry, no Texas.")
    
# get a city with a default value
city = cities.get('TX', 'Does Note Exist')
print("The city for the state 'TX' is: %s" % city)

x = None
if not x:
    print("x is empty")
