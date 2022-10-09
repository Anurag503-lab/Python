# iteration over the list and 

#1: Using For loop
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
# Using for loop
for i in list:
    print(i)
    
    
#2: For loop and range()

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
# getting length of list
length = len(list)
# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    print(list[i])
    
    
#3: Using while loop
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
# Getting length of list
length = len(list)
i = 0# Iterating using while loop
while i < length:
      print(list[i])
      i += 1