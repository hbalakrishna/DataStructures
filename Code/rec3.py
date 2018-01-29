a = [2,3,4,4,4]

# # if 2 in a:
# #     a.remove(a.index(2))
# val = 4
#
# b = a
#
# b = [i for i in a if i!= val]
#
# print(b)


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    b = [i for i in nums if i != val]
    return b
