nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
k = m+n-1


while m>0 and n>0:
    if nums1[m-1]>=nums2[n-1]:
        nums1[k] = nums1[m-1]
        m = m - 1
        k = k-1
    else:
        nums1[k] = nums2[n-1]
        n = n - 1
        k = k -1

if n > 0:
    nums1[:n] = nums2[:n]

print(nums1)
