def gapInsert(a, start, gap):
    for i in range(start+gap, len(a),gap):
        pos = i
        curr = a[i]

        while pos >=gap and a[pos-1]>curr:
            a[pos] = a[pos-gap]
            pos = pos - gap
        a[pos] = curr


def shellSort(a):
    sublist = len(a)//2

    while sublist > 0:

        for start in range(sublist):
            gapInsert(a,start,sublist)
        sublist = sublist//2

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)



