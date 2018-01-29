nums = [1,2,2,3,4,3,5,6,7]
d = {}
a = []
b = []

for i in nums:
    d[i] = d.get(i, 0) + 1

print(d)

for k, v in d.items():
    if v == 2:
        a.append(k)

b = [k for k, v in d.items() if v ==2]
print(b)
