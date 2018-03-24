nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]

result = []

for i in nums1:
    idx_ = nums2.index(i)
    print(idx_)
    if idx_+1 > len(nums2) - 1:
        result.append(-1)
    elif max(nums2[idx_:]) > i:
        result.append(nums2[idx_ + 1])
    else:
        result.append(-1)

print(result)
print(max(nums2[idx_:]))