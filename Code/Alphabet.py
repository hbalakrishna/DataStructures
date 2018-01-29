a = ["Hello", "Alaska", "Dad", "Peace"]
a1 = 'qwertyuiop'
a2 = 'asdfghjkl'
a3 = 'zxcvbnm'
r = []
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in a:
    x = i.lower()
    l = len(x)
    for j in x:
        if j in a1:
            cnt1+=1
        elif j in a2:
            cnt2+=1
        elif j in a3:
            cnt3+=1

    if cnt1 == l or cnt2==l or cnt3==l:
        r.append(i)
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0


print(r)