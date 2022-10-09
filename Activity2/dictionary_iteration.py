#1.Access key using the build .keys()

# Python code to iterate through all values in a dictionary
statesAndCapitals = {
'Gujarat': 'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan': 'Jaipur',
'Bihar': 'Patna'
}
keys = statesAndCapitals.keys()
print(keys)


#2:Access key without using a key()

# Python code to iterate through all keys in a dictionary
statesAndCapitals = {
'Gujarat': 'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan': 'Jaipur',
'Bihar': 'Patna'
}
print('List Of given states:\n')
# Iterating over keys
for state in statesAndCapitals:
    print(state)

#3:Iterate through all values using .values()

# Python code to iterate through all values in a dictionary
statesAndCapitals = {
'Gujarat': 'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan': 'Jaipur',
'Bihar': 'Patna'
}
print('List Of given capitals:\n')
# Iterating over values

for capital in statesAndCapitals.values():
    print(capital)


#4: Iterate through all key, and value pairs using items()

# Python code to iterate through all key, value
# pairs in a dictionary
statesAndCapitals = {
'Gujarat': 'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan': 'Jaipur',
'Bihar': 'Patna'
}
print('List Of given states and their capitals:\n')
# Iterating over values
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)


#5:Access both key and value without using items()

# Python code to iterate through all values in a dictionary

statesAndCapitals = {
'Gujarat': 'Gandhinagar',
'Maharashtra': 'Mumbai',
'Rajasthan': 'Jaipur',
'Bihar': 'Patna'
}
for i in statesAndCapitals:
    print(i, '->', statesAndCapitals[i])
