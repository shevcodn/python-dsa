def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums

def remove_element(nums, val):
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return nums[:left]

def compress_array(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] is not None:
            nums[left] = nums[right]
            left += 1
    return nums[:left]

def partition_by_sign(nums):
    positive = [x for x in nums if x > 0]
    negative = [x for x in nums if x < 0]
    zeros = [x for x in nums if x == 0]
    return negative + zeros + positive

print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([0, 0, 1]))
print(move_zeroes([1, 0, 2, 0, 0, 3]))

print(remove_element([3, 2, 2, 3, 4, 3, 5], 3))
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))

transactions = [150.0, 0, -30.0, 0, 200.0, 0, -50.0]
print("Clean non-zero transactions:", remove_element(transactions[:], 0))
print("Partitioned by direction:", partition_by_sign(transactions))

feed_data = [1.08, None, 1.09, None, None, 1.07]
print("Valid price feed:", compress_array(feed_data))
