nums = [1,3,5,6]
target = 5

if target in nums:
    print(nums.index(target))
elif target > max(nums):
    print(nums.index(max(nums)) + 1)
elif target < min(nums):
    print(nums.index(min(nums)))
else:
    for i in range(len(nums) - 1):
        if target > nums[i] and target < nums[i + 1]:
            print(i + 1)
