# List is an ordered collection of data that is changeable (items can be change, add, and remove items in a list after it has been created)
# they are created using square brackets: [ ]

mylist = ["apple","banana","cherry"]
# print(mylist)

# they also allow duplicate items (items of the same value) be stored in them

dup = ['a','b','a','b']
# print(dup)

# len() function is to determinge how many items are in a list

check_length = ['a','b','c','d','e','f']
# print(len(check_length))

# list() is a constructor when creating a new list

characters = list("helloworld")
print(characters)
# output is ['h','e','l','l','o','w','o','r','l','d']

grocery_list =list(('apple','pear','milk'))
print(grocery_list)
# output is ['apple','pear','milk']