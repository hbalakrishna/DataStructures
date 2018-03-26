def countandsay(n):
    s = '1'
    for i in range(1,n):
        c = 1
        t = []
        for j in range(1, len(s)):
            if s[j] == s[j-1]:
                c += 1
            else:
                t.append(str(c))
                t.append(s[j-1])
                c = 1
        t.append(str(c))
        t.append(s[-1])
        s = ''.join(t)
    return s


print(countandsay(3))




