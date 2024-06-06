# # creating a list 
# myList= [] #Empy list 

# print(type(myList))


# fruits=["apple","banana","mango","pineapple","guava"]
# print(f"Length of list of fruits is:  {len(fruits)}")

# # adding an aelement is list 
# fruits.append("orange")

# print(f"Fruits after appending: {fruits}")

# fruits.insert(0,"berry")
# print(f"fruits after inserting berry in position 1: {fruits}")

# # removing elements from list:

# # removing one element 

# popped_element = fruits.pop()
# print(f"Popped element is: {popped_element}")
# print(f"The list after popping is:{fruits}")


# fruits.remove("mango")
# print(f"After removing:{fruits} ")

# concatination of lists
list1= [1,2,3]
list2= [4,5,6]
lists=list1+list2
print(f"list is: {lists}")

# concatination of list using extend function
list3=[1,2,3]
list4=[4,5,6]
list3.extend(list4)
print(f"List after concatination: {list3}")

# slicing in list
list5 =[1,2,3,4,5,6]
first=list5[0]
second=list5[1]
third= list5[2]

sublist = list5[1:6:2] 
print(f"Sublist: {sublist}")

# negative indexing
last_element = list5[-1]
print(f"last element of list5: {last_element}")

second_last_element= list5[-2]
print(f"second last element is: {second_last_element}")

sublist1=list5[-4:5]
print(f"sublist1: {sublist1}")

reversed_list= list5[::-1]
print(f"reversed list: {reversed_list}")

# nested list
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(type(nested_list))
print(f"Nested list: {nested_list}")
first_element=nested_list[0]
print(f"First element of nested list: {first_element}")

print(f"First and first element of nested list is: {nested_list[0][0]}")











