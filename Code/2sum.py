nums = [2, 7, 11, 15]
target = 9
d = {}

for i, num in enumerate(nums):
    if target - num in d:
        print(d[target - num] + 1, i + 1)
    d[num] = i


# for i in range(len(nums)):
#     target_ = target - nums[i]
#     nums[i] = "$"
#     if target_ in nums:
#         # ans.append(i + 1)
#         idx1 = i + 1
#         # ans.append(nums.index(target_) + 1)
#         idx2 = nums.index(target_) + 1
#         break

# print(idx1, idx2)