def count_digit(m):
    return count_digit_helper(m,10,1)

def count_digit_helper(m,n, i):
    if (m%n==m):
        return i
    else:
        i+=1
        n = pow(n, i)
        return count_digit_helper(m, n, i)

print(count_digit(50))
print(count_digit(9))
print(count_digit(298))

