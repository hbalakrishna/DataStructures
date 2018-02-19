a = [1,1,2,2,3]

res = set()

i = 0

while i < (len(a) - 1):
    if a[i] is a[i+1]:
        del a[i]
    else:
        i += 1
print(len(a))

a = list(set(a))
print(a)