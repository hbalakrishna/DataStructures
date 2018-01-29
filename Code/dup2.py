a = [1,1,2]
d = {}

for i in a:
    d[i] = d.get(i, 0) + 1

for k, v in d.items():
    if v == 1:
        print(k)
        exit(0)
