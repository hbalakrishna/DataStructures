nums1 = [1, 2]
nums2 = [3, 4]
result = []
for i in nums1:
    if i not in result and i in nums2:
        result.append(i)

print(result)
