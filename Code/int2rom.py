a = 100
ans = ""
d = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
# for i in range(len(str(a))):
#     print(str(a[i]))
#     print(d[str(a[i])])

while a > 10:
    ans += d[10]
    a = a - 10

ans += str(d[a])

print(ans)

strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ret = ""
for i, j in enumerate(nums):
    while a >= j:
        ret += strs[i]
        a -= j
    if a == 0:
        print(a)

print(ret)