#Method 1 : Using isalpha() + len()
test_str="geeksforgeeks !!$ is best 4 all Geeks 10-0"
# printing original string
print("The original string is :" + str(test_str))
# isalpha() to computation of Alphabets
res = len([ele for ele in test_str if ele.isalpha()])
# printing result
print("Count of Alphabets :" + str(res))

#Method 2 : Using ascii_uppercase() + ascii_lowercase() + len()
import string
# initializing string
test_str1="geeksforgeeks !!$ is best 4 all Geeks 10-0"
# printing original string
print("The original string is :" + str(test_str1))
# ascii_lowercase and ascii_uppercase
res = len([ele for ele in test_str1 if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
# printing result
print("Count of Alphabets :" + str(res))

# initializing list
test_list = ["geeksforgeeks", "is" , "best" , "for" , "geeks"]
print("The original list is :" + str(test_list))
# initializing char range
strt, end = 14,30
# strt and end used to get desired characters
res = ".join([sub for sub in test_list])[strt : end]"
# printing result
print("Range characters : " + str(res))

#Example 1: More examples on Python String isalnum() Method
string = "abc 123"
print(string, "is alphanumeric?", string.isalnum())
string ="abc_123"
print(string, "is alphanumeric?", string.isalnum())
string = "000"
print(string, "is alphanumeric?", string.isalnum())
string ="aaaa";
print(string, "is alphanumeric?", string.isalnum())