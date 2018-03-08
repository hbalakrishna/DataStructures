a = "geeks"
b = "geek"
c = ["aa","ab"]

if not c:
     print("")

if len(c) == 1:
    print(c)

cmp = ""
for i in range(len(c) - 1):
    if c[i + 1] in c[i]:
        cmp = c[i]

print("".join(cmp))