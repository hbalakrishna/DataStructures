

a = [0,1,2,3,4,5,6,7,0]
sum_c = 5

for i in range(len(a) - 1):
    j = i + 1
    while j<len(a):
        if (a[i] + a[j] == sum_c):
            print(i, j)
            exit(0)
        j = j+1



