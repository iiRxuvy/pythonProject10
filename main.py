#SECTION #1
color_list = ["red", "green", "blue", "yellow"]
#TODO: use notes to print first element
print("First element:", color_list[0])
#TODO: use notes to print last element
print("Last element:", color_list[-1])

#SECTION #2
# TODO: create num_list
num_list = [4, 6, 4, 2, 9, 4, 1]
#TODO: use append to add 5 to num_list and print
num_list.append(5)
print("After appending 5:", num_list)
#TODO: use remove to remove the
num_list.remove(4)
print("After removing first 4:", num_list)
# first occurence of 4 and then print
#TODO: use count to count how many times 4 appears in num_list
count_of_4 = num_list.count(4)
print("Count of 4:", count_of_4)
#TODO: use the index method to find where the 9 is and print the index
index_of_9 = num_list.index(9)
print("Index of 9:", index_of_9)

#SECTION #3
#TODO: first part of section 3
fruit_list = ["apple", "banana", "cherry"]
#TODO: use index operator [] to alter index 1 to orange.  Use notes
fruit_list[1] = "orange"
print("After changing bana to orange:", fruit_list)
fruit_list.pop()
print("After popping the last element:", fruit_list)