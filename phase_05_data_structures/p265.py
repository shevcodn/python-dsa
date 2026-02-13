def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(123))
print(sum_digits(9999))
print(sum_digits(0))
print(sum_digits(100))

