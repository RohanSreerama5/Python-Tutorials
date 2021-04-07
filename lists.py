# Lists: ordered, mutable, allows duplicate elements 
# a collection type 

mylist = ["banana", "cherry", "apple"]
# print(mylist)

# create new empty list with list() function 
mylist2 = list()
# print(mylist2)

# list allows for different datatypes and duplicate elements
mylist3 = [5, True, "apple", "apple"]
# print(mylist3)

# index list to get elements 
item = mylist[0]
# print(item)

# can also specify negative index, ie. -1 refers to last item in list
# print(mylist[-1])
# -2 is second  last item and so on 

# iterate over list with for in loop 
for i in mylist:
    print(i)

# check if an item is in list 
if "banana" in mylist:
    print("yes")
else:
    print("no")


# get length of list 
print(len(mylist))

# append items to list 
mylist.append("lemon") # inserts at end of list 
print(mylist)

# inserts element at specified index
mylist.insert(1, "blueberry") # shifts over other items to make it work 
print(mylist) 

item2 = mylist.pop() # removes last element from list and returns it 
print(item2) 

# removed specific element by its value 
mylist.remove("cherry") # removes cherry and shifts down other elements 

# remove all elements 
mylist.clear() 

# reverse the list 
mylist.reverse() 

# sort the list 
newlist = [4, 3, 1, -1, -5, 10]
# newlist.sort() # sorts in place 
# print(newlist) # newlist now in ascending order 

# if u want to keep orig list but get a new diff one thats sorted use
new_list_sorted = sorted(newlist) 
print(newlist)
print(new_list_sorted)

# suppose u want a list with all 0's in it and 5 elements total 
rlist = [0] * 5 
print(rlist) 

# concat 2 lists with + operator 
aList = [1, 2, 3, 4, 5] 

combineList = rlist + aList 
print(combineList)

# slicing - way to access subparts of list with colon : 

glist = [1, 2, 3, 4, 5, 6 ,7, 8, 9]

a = glist[1:5] # specify start index as 1 and stop index as 5 
# stop index is not inclusive, so it actually prints from idx 1-4
print(a) 

b = glist[:5] # if u don't specify start idx, it auto starts from beginnng 
print(b) 

c = glist[1:] # if u dont specify stop idx, it goes all the way to end 
print(c) 

# step index feature 
d = glist[::2] # now prints every other item starting from start element 
# step index can also be a bigger number, by default it is 1 
print(d)

# can also specify negative step index to reverse the list 
e = glist[::-1] # steps backward now 
print(e) 

# copying a list 
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
print(list_cpy) 

# so now if u just assign copy to original like that, then when 
# u modify the copy it also modifies the original list becuase 
# list_cpy just became a pointer to orig list in memory 

list_cpy.append("lemon") 
print(list_cpy)
print(list_org) # both now have "lemon"

# to make independent copy of list, use .copy() 
list_actual_cpy = list_org.copy() 
list_actual_cpy.append("new")
print(list_actual_cpy) 
print(list_org)

# another way to do this is using list() func 
list_actual_cpy = list(list_org) 

# a third way to do this is slicing 
list_actual_cpy = list_org[:] # copies list from start to end since start and end 
# indices not specified 

# IMPORTANT TRICK 
# list comprehension - fast way to create new list from existing list with one line
jList = [1, 2, 3, 4, 5, 6]
b = [i*i for i in jList] # quikcly makes a new array with jList's values squared
# syntax: expression then for-in loop over your orig list

print(jList)
print(b) 

