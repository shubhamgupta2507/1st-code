

# Create a List
# A list of three elements
ages = [19, 26, 29]
print(ages)

# Perform a operations
#    1  Access Element
languages = ['Python', 'Swift', 'C++']

# access the first element
print(languages[0])

# access the third element
print(languages[2])

#    2  Add Element
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

# using append method
fruits.append('cherry')

print('Updated List:', fruits)

#   3   Change the element or item
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# changing the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)

#  4  Remove the element
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers)

# Output: [2, 7, 9

# creating a dictionary
country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}

# printing the dictionary
print(country_capitals)

#   2 Access value
country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])
print(country_capitals["England"])

# 3  add item
country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
}

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"

print(country_capitals)

#   4   remove item
country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
}

# delete item having "Germany" key
del country_capitals["Germany"]

print(country_capitals)

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

#  1  add number
numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers)

#   2  modified
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)

