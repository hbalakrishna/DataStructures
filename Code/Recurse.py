x = 1563847412
n = x
ans = ""
n = str(n)
set_1 = 0

n = str(x)
count = 0

if n[0] == "-":
    set_1 = 1
    n = n[1:]

len_str = len(n)
for i in range(len_str):
    if len_str>=0:
        ans+= (n[len_str - 1] )
        len_str = len_str - 1

if ans[0] == "0":
    ans = ans[1:]

if set_1 == 1:
    ans = "-" + ans

if x == 0 or int(ans).bit_length()>=32:
    print(int(0))
else:
    print(int(ans))




