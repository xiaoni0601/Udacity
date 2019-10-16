# Question 1: Pick One

# Define a procedure, pick_one, that takes three inputs: a Boolean 
# and two other values. If the first input is True, it should return 
# the second input. If the first input is False, it should return the 
# third input.

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

def pick_one(first, second, third):
    if first is True:
        return second   #true_response
    else:
        return third    #False_response

print(pick_one(True, 37, 'hello'))
#>>> 37

print(pick_one(False, 37, 'hello'))
#>>> hello

print(pick_one(True, 'red pill', 'blue pill'))
#>>> red pill

print(pick_one(False, 'sunny', 'rainy'))
#>>> rainy

# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

def triangular(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result   


print(triangular(1))
#>>>1

print(triangular(3))
#>>> 6

print(triangular(10))
#>>> 55


# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(text):
    while '<' in text:
        text = text [0:text.find('<')] + " "+ text [text. find('>')+1:]
    return text.split()
    


print(remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''))
#>>> ['Title','This','is','a','link','.']

print(remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>'''))
#>>> ['Hello','World!']

print(remove_tags("<hello><goodbye>"))
#>>> []

print(remove_tags("This is plain text."))
#>>> ['This', 'is', 'plain', 'text.']

#####. another way:
def remove_tags(string):
    start = string.find('<')
    while start != -1:
        end = string.find('>', start)
        string = string[:start] + " " + string[end + 1:]#去掉起始tag
        start = string.find('<')
    return string.split()