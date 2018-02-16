
d = 12

ans = set()

while d!=1:
    d = sum([int(i)**2 for i in str(d)])
    if d in ans:
        print(False)
    else:
        ans.add(d)

else:
    print(True)





