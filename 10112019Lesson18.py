#time_exection
#spin_loop
import time
def time_exection(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time
def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
    
# hash_function
print(ord('a'))
print(ord('A'))
print(chr(ord('a')))

# Modulus_quiz
print(12 % 3)
print(ord('a') % ord('a'))
print((ord('z') + 3) % ord('z'))