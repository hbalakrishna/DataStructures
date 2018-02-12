a = [2,2]
min_ = 1
max_ = len(a)
b = []

if not b:
    print('Empty')

# Time limit exceeded
res = [i for i in range(1, max_ + 1) if i not in a]
print(res)

#set minus set
print(list(set(range(1, max_ + 1)) - set(a)))

