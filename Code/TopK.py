import operator
a = [1,1,1,2,2,3]
k = 2
d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


# print(d.items())

final_sort = sorted(d.items(), key=lambda x:x[1], reverse=True)
sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
sorted_dict = sorted(d.items(), key = lambda k : k[1], reverse=True)

print(sorted_d)
print(list(sorted_dict[:2]))
print(list(sorted_dict[:2][0]))
# print(d)
# print(list(d.keys())[:2])
res = []
for k,v in sorted_d[:2]:
    res.append(k)

print(res)

