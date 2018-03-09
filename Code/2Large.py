nums = [3, 6, 1, 0]

max_ = max(nums)
pos_ = nums.index(max_)
nums.pop(nums.index(max_))

for i in nums:
    if i * 2 <= max_:
        pass
    else:
        pos_ = -1
        break

print(nums, max_, pos_)