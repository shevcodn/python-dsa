def climb_stairs(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
    return b

print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(5))
