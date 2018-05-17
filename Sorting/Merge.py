a = [10,20,40,50, 15,25,30]
# b = [15,25,30]
# mid = int(len(a)/2)
# low = 0
# i, j, k = low,mid + 1,low
n = len(a)
# m = len(b)
c = [None] * (n)

# print(i,j,k)

def MergeSort(a, low, high,mid):
    i, j, k = low, mid + 1, low
    while i <= mid and j <=high:
        if a[i] < a[j]:
            c[k] = a[i]
            i = i + 1
            k = k + 1
        else:
            c[k] = a[j]
            j = j + 1
            k = k + 1
    while i<=mid:
        c[k] = a[i]
        i = i + 1
        k = k + 1
    while j<=high:
        c[k] = a[j]
        j = j + 1
        k = k + 1

    for i in range(low, high):
        a[i] = c[i]

def Merge(a):
    if len(a)>1:
        mid = (len(a))//2
        lhalf = a[:mid]
        rhalf = a[mid:]

        Merge(lhalf)
        Merge(rhalf)
        i,j,k=0,0,0
        # print(low,mid,high)
        while i <len(lhalf) and j <len(rhalf):
            if lhalf[i] < rhalf[j]:
                a[k] = lhalf[i]
                i = i + 1
            else:
                a[k] = rhalf[j]
                j = j + 1
            k = k + 1
        while i<len(lhalf):
            a[k] = lhalf[i]
            i = i + 1
            k = k + 1
        while j<len(rhalf):
            a[k] =rhalf[j]
            j = j + 1
            k = k + 1



alist = [10,20,40,50, 15,25,30]
Merge(alist)
print(alist)


