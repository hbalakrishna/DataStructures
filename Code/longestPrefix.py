a = ["geeksforgeeks","geeks","geek"]

if not a:
    print("")

if len(a) == 1:
    print(a)

cmp_ = a[0]

i = 1

while i<len(a):
    j = 0
    k = 0

    while j < len(cmp_) and k < len(a[i]):
        if cmp_[j] != a[i][k]:
            cmp_ = cmp_[0:j]
            break
        j += 1
        k += 1
    cmp_ = cmp_[0:j]
    i += 1

print(cmp_)
