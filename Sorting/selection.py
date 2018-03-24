# a = [2,5,4,6]
#
# for i in range(len(a) - 1):
#     min_ = i
#     for j in range(i+1, len(a)):
#         if a[j] < a[min_]:
#             min_ = j
#     t = a[i]
#     a[i] = a[min_]
#     a[min_] = t
#
# print(a)
def smallest(x, y, z):
    c = 0

    while (x or y or z):
        x = x - 1
        y = y - 1
        z = z - 1
        c = c + 1

    return c


# Driver Code
x = 12
y = 15
z = 5
print("Minimum of 3 numbers is",
      smallest(x, y, z))
