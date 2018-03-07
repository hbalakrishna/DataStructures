from math import ceil, floor

nums1 = [1, 2]
nums2 = [3, 4]


merged = sorted(nums1 + nums2)

if len(merged)%2==0:
    print((merged[int(len(merged)/2)] + merged[int((len(merged)/2)-1)])/2.0)

else:
    print(float(merged[floor(len(merged)/2)]))

