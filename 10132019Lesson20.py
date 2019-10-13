# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    letter_index = ord(letter) - ord('a')
    shifted_index = (letter_index + n) % 26 
    return chr(ord('a') + shifted_index)

print(shift_n_letters('s', 1))
#>>> t
print(shift_n_letters('s', 2))
#>>> u
print(shift_n_letters('s', 10))
#>>> c
print(shift_n_letters('s', -10))
#>>> i


# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
def shift_n_letters(letter, n):
    letter_index = ord(letter) - ord('a')
    shifted_index = (letter_index + n) % 26 
    return chr(ord('a') + shifted_index)

def rotate(words, n):
    result = ''
    for letter in words:
        if letter  == ' ':
            result = result + ' '
        else:
            letter_result = shift_n_letters(letter,n)
            result = result + letter_result
    return result
            
    # Your code here

print(rotate ('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu',13))
#>>> 'sarah'
print(rotate('dave',5))
#>>>'ifaj'
print(rotate('ifaj',-5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???