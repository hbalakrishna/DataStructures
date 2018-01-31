J = "aA"
S = "aAAbbbb"
words = zip(J, S)
a = []
# print(len([c for c,d in words if c==d]))
print(list(J))
for i in list(J):
    for j, ltr in enumerate(list(S)):
        if ltr == i:
            a.append(j)

print(len(a))





