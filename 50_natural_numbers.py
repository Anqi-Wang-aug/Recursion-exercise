def natural_numbers(num):
    if(num == 1):
        print(num, end = ' ')
    else:
        natural_numbers(num-1)
        print(num, end = ' ')
        
natural_numbers(50)
