a = [1,1,0,1,1,1]

res = []
j = 0
for i in a:
    if i == 1:
        j += 1
    else:
        res.append(j)
        j = 0
res.append(j)

print(max(res))