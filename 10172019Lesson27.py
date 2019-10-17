# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

# 拆解：由题目中的月/日/年转化为日 月 年。方法：

def date_converter(language, date):
    first = date.find('/')    # 1.寻找日期中的‘/’
    month = date[:first]      # 2. month等于first之前的所有内容，并且不包含‘/’符号
    second = date.find('/', first + 1) #3.从first之后的下一个位置开始找第二个‘/’
    day = date[first + 1 : second]     #4.day等于第二个‘/’之前，第一个‘/’之后的所有内容
    year = date[second + 1 :]          #5.year等于第二个‘/’之后的下一个位置的所有内容
    return(day + " " + language[int(month)] + " " + year)

print(date_converter(english, '5/11/2012'))
#>>> 11 May 2012

print(date_converter(english, '5/11/12'))
#>>> 11 May 12

print(date_converter(swedish, '5/11/2012'))
#>>> 11 maj 2012

print(date_converter(swedish, '12/5/1791'))
#>>> 5 december 1791

#another simple way: with split
english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

def date_converter2(language, date):
    month, day, year = date.split('/')
    return day + " " + language[int(month)] + " " + year
print(date_converter2(english, '5/11/2012'))
#>>> 11 May 2012

print(date_converter2(english, '5/11/12'))
#>>> 11 May 12

print(date_converter2(swedish, '5/11/2012'))
#>>> 11 maj 2012

print(date_converter2(swedish, '12/5/1791'))
#>>> 5 december 1791




# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return [match, replacement]



def apply_converter(converter, string):
    previous = None           #跟踪之前的string；起始不存在precious，因此无需while-loop
    while previous != string: #有了previous，而且previous与目前的string不同，即进入while-loop
        previous = string     #
        position = string.find(converter[0])  #寻找string中match部分
        if position != -1:   # if成立，类似Boolean
            string = string[:position] + converter[1] + string[position + len(converter[0]) :]  #找到之后进行替换，并结合剩下部分生成新的string，循环到最后无法match与替换为止
    return string  #得到最终的string输出
        

# For example,

c1 = make_converter('aa', 'a')
print(apply_converter(c1, 'aaaa'))
#>>> a

c = make_converter('aba', 'b')
print(apply_converter(c, 'aaaaaabaaaaa'))
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).


# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(input_list):
    best_element = None
    length = 0
    current = None
    current_length = 0
    for element in input_list:
        if current != element:
            current = element
            current_length = 1
        else:
            current_length = current_length + 1
        if current_length > length:
            best_element = current
            length = current_length
    return best_element


#For example,

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print(longest_repetition([1,2,3,4,5]))
# 1

print(longest_repetition([]))
# None





# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(p):
    if not is_list(p):
        return p   # base case
    else:
        result = []
        for i in range(len(p) - 1, -1, -1):    # range(from, to, step)
            result.append(deep_reverse(p[i]))   # recurse 递归
        return result

#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print(deep_reverse(p))
#>>> [[[[6, 5], 4], 3, 2], 1]
print(p)
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print(deep_reverse(q))
#>>> [ [6,5], 4, [3, 2], 1]
print(q)
#>>> [1, [2,3], 4, [5,6]]