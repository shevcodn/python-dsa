def permutations(nums):
    result = []
    def backtrack(current, used):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if i in used:
                continue
            current.append(nums[i])
            used.add(i)
            backtrack(current, used)
            current.pop()
            used.remove(i)
    backtrack([], set())
    return result

print(permutations([1,2,3]))
print(permutations([1,2]))