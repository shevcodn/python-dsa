def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)

    return fib_sequence[-1]

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(6))
print(fibonacci(10))