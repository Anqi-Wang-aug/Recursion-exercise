import sys

def fib(num):
    if(num == 0):
        result = 0
    elif (num ==1):
        result = 1
    else:
        result = fib(num-1)+fib(num-2)
    return result

for i in range(10):
    print(fib(i), end = ' ')

    
