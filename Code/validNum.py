ip = ["1","C","-62","-45","-68"]
valid = []
for a, b in zip(ip, ip[1:]):
    if a == "C":
        valid.remove(valid[-1])
    elif a == "D":
        valid.append(valid[-1] * 2)
    elif a  not in ("C", "D", "+"):
        valid.append(int(a))
    else:
        valid.append(valid[-1] + valid[-2])

if b == "C":
    valid.remove(valid[-1])
elif b == "D":
    valid.append(valid[-1] * 2)
elif b == "+":
    valid.append(valid[-1] + valid[-2])
else:
    valid.append(int(b))

print(sum(valid))

# ip = ["5","-2","4","C","D","9","+","+"]
# va = []
# for a, b in zip(ip, ip[1:]):
#     if a not in ("C","D","+"):
#         va.append(a)
#
# print(va)

# print(valid)
from functools import reduce

# ab = [1,2,3]
# r = []
# # for i in range(1,len(ip)):
# #     print(ip[i-1], ip[i])
# #     if ip[i] == "C":
# #         valid.remove(int(ip[i-1]))
# print(r.append(ab[-1] * 2))
# print(r)


