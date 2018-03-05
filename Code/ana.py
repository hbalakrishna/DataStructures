A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
P = []

for i in A:
    if i in B:
        idx = B.index(i)
        P.append(idx)
        B[idx] = 'x'

print(P)
