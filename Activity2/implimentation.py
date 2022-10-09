#implementation of List and Dictionary

#1. Program to Find Even Numbers From a List
list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
for i in list2:
    if i % 2 == 0:
     print(i)

#2. Interchange First and Last Element of a List
list5 = [1, 29, 51, 9, 17, 6, 7, 23]
list5[0], list5[-1] = list5[-1], list5[0]
print(list5)

#3. Program to Merge Two Lists
list3 = [1, 2, 4, 6]
list4 = [9, 3, 19, 7]
list3.extend(list4)
print(list3)

#Creating Dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)

#Accessing the dictionary values
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print("Name : %s" %Employee["Name"])
print("Age : %d" %Employee["Age"])
print("Salary : %d" %Employee["salary"])
print("Company : %s" %Employee["Company"])


#Deleting elements using del keyword
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
print("Deleting some of the employee data")
del Employee["Name"]
del Employee["Company"]
print("printing the modified information ")
print(Employee)