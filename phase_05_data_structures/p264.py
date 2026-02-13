def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        return base * power(base, exp - 1)
    
print(power(2, 10))
print(power(3, 3))
print(power(5, 0))
print(power(2, 1))