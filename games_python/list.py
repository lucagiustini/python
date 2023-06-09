data = ["apple", "mango", "oranges"]
print(data)
# to find length of list in python
print(len(data))


print("List in Python")
myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
# will display all items in the list
print(myList)
# will display items at some range
print(myList[1:4])
print(myList[4:6])

# also in reverse direction
print(myList[:-1])
print(myList[4:-1])

# to update the value of specific item
myList[2] = 99
print(myList)


# to add new value at the end
myList.append(1002)
print(myList)
# to remove item
print(myList)
myList.remove(8)  # will remove first occurrence of 8
print(myList)

# to sort list
myList.sort()
print(myList)

# to reverse list
myList.reverse()
print(myList)

abc = ["abc", "Hello", "between"]
# to check if something is in the list or not
print(999 in myList)
print(4 in myList)
print(6 in myList)
print(2 in myList)
print("Hello" in abc)

# to add new value at the end
myList.append("luca")
print(myList)


# converting list of string to integer
string_list = ['4', '5', '87', '6']
integer_list = [int(element) for element in string_list]
print(integer_list)
print(type(integer_list[0]))


# converting list of string to integer using map
string_list = ['4', '5', '87', '6']
integer_list = list(map(int, string_list))
print(integer_list)
print(type(integer_list[1]))