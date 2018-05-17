def insertionSort(a):
   for i in range(1,len(a)):
        pos = i
        curr = a[i]

        while pos>0 and a[pos-1]>curr:
            a[pos] = a[pos-1]
            pos = pos - 1
        a[pos] = curr

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)