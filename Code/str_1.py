a = "abcdef"
b = "abcd"

for i in range(len(a) - len(b) + 1):
    if a[i:i+len(b)] == b:
        print(i)
print(-1)