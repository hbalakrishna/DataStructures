n = 15
ans = []
for i in range(1,16):
    if i % 3 == 0 and i % 5 == 0:
        ans.append("FB")
    elif i % 5 == 0:
        ans.append("B")
    elif i % 3 == 0:
        ans.append("F")
    else:
        ans.append(str(i))

print(ans)
