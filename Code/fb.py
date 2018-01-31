# n = 15
# ans = []
# for i in range(1,16):
#     if i % 3 == 0 and i % 5 == 0:
#         ans.append("FB")
#     elif i % 5 == 0:
#         ans.append("B")
#     elif i % 3 == 0:
#         ans.append("F")
#     else:
#         ans.append(str(i))
#
# print(ans)
from numpy import mean

a = [89,72,94,69]
max_ = max(a)
min_ = min(a)
avg_ = mean(a)

print(avg_, max_,min_)
print((89 - avg_) / (max_  - min_))
