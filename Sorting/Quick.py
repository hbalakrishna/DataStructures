def quickSort(a, low, high):
    pivot = a[low]
    i = low + 1
    j = high

    while(1):
        while pivot>=a[i] and i<high:
            i = i +1
        while pivot<=a[j] and j>low:
            j = j - 1

        if i < j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        else:
            temp = a[j]
            a[j] = a[low]
            a[low] = temp
            return j



def qhelper(a,low,high):
    if low < high:
        j = quickSort(a, low, high)
        qhelper(a,low, j-1)
        qhelper(a,j+1,high)

def qSort(a):
    qhelper(a, 0, len(a) -1)

alist = [54,26,93,17,77,31,44,55,20]
qSort(alist)
print(alist)
