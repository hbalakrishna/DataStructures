
x = -111

# s = (x > 0) - (x < 0)
# #print(s)
# r = int(str(x*s)[::-1])
# print(r)
# print(s*r * (r < 2**31))

set_1 = 0
x = str(x)
if x[0] == "-":
    set_1 = 1
    x = x[1:]

r = (str(x)[::-1])
print(r)
if set_1 == 1:
    r = "-"+r


x= int(x)
r = int(r)
s = (x > r) - (x < r)
print('x'[::])


