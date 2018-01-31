a = [1,4,3,2]
b1 = sorted(a)
for a, b in zip(b1[::2], b1[1::2]):
    print(min((a,b)))

#rint(sum([min(a, b) for a, b in zip(b1[::2],b1[1::2])]))

print(b1[::2])
