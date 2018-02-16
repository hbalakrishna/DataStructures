nums = [3,2,4]
target = 6

ans = []

for i in range(len(nums)):
    target_ = target - nums[i]
    nums[i] = "$"
    if target_ in nums:
        ans.append(i)
        ans.append(nums.index(target_))
        break

print(ans)