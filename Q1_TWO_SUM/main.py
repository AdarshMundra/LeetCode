def twoSum(array, target):
    nums = {}
    for i, num in enumerate(array):
        d =target - num
        if d in nums:
            return [nums[d], i]
        nums[num] = i
    return []

print(twoSum([2,7,11,15], 9))