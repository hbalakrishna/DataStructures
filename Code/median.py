nums1 = [1, 2]
nums2 = [3, 4]

merged = nums1 + nums2


len_ = len(merged)
if not (float(len_/2)).is_integer():
    print(merged[int(len_/2)])
else:
    print((merged[int(len_/2)] + merged[int(len_/2) - 1])/2)