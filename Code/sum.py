

a = [0,1,2,3,4,5,6,7,0]
sum_c = 5

def func_sum(a, sum_c):
    for i in range(len(a) - 1):
        j = i + 1
        while j<len(a):
            if (a[i] + a[j] == sum_c):
                return [i, j]
                exit(0)
            j = j+1


print(func_sum(a, sum_c))
