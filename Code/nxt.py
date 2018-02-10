nums1 = [1,3,5,2,4]

nums2 = [6,5,4,3,2,1,7]




res = []

max_ = max(nums2)
print(max_)
print(len(nums2))
print(nums2.index(1))

for i in range(len(nums1)):
    in_place = nums2.index(nums1[i])
    if in_place == len(nums2) - 1 or nums2[in_place] == max_ or nums1[i]>nums2[in_place + 1]:
        res.append(-1)
    else:
        res.append(nums2[in_place + 1])

print(res)