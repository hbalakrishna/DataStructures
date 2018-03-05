d = {'U':1, 'D':-1, 'R':1, 'L':-1}

ip = "LL"
origin = 0

for i in ip:
    origin += d[i]

print(origin)
if origin==0:
    print('Yes')
else:
    print('No')