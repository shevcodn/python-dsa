def length_of_lis(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

def length_of_lis_binary(nums):
    sub = []
    for num in nums:
        left, right = 0, len(sub)
        while left < right:
            mid = (left + right) // 2
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(sub):
            sub.append(num)
        else:
            sub[left] = num
    return len(sub)

print(length_of_lis([10,9,2,5,3,7,101,18]))
print(length_of_lis([0,1,0,3,2,3]))
print(length_of_lis([7,7,7,7]))

print(length_of_lis_binary([10,9,2,5,3,7,101,18]))
print(length_of_lis_binary([0,1,0,3,2,3]))