
# Q1. sum_list
# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.
def sum_list(list):
    result = 0
    for element in list:
        result= result + element
    return result
print(sum_list([1, 7, 4]))
print(sum_list([9, 4, 10]))
print(sum_list([44, 14, 76]))

# Q2. measure_udacity
# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.
def measure_udacity(U):
    count = 0
    for element in U:
        if element[0] == 'U':
            count = count + 1
    return count
 
print(measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

print(measure_udacity(['Umika','Umberto']))
#>>> 2

#Q3.  find_element
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
# while-loop:
def find_element(list, target):
    i = 0
    while i < len(list):
        if list[i] == target:
            return i
        i = i + 1
    return -1

print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))
#>>> -1

# if-loop:
def find_element(p, t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return - 1
print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))  


# if-in:
def find_element(li,el):
    if el in li:
        return li.index(el)
    return -1
print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))  

# if-not-in:
def find_element(li,el):
    if el not in li:
        return -1
    else:
        return li.index(el)
print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))  


