def max_heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] > A[i]:
        largest = left

    if right <n and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]

        max_heapify(A,n,largest)

def heapSort(A):
    n = len(A)

    for i in range(n, -1, -1):
        max_heapify(A, n, i)
    print(A, n)
    for i in range(n-1,0,-1):
        A[i], A[0] = A[0], A[i]
        print("Before",A)
        print("Before A[i]",A[i])
        print("Before A[0]",A[0])
        max_heapify(A,i,0)
        print("After",A)
        print("After A[i]",A[i])
        print("After A[0]",A[0])



A=[12, 11, 13, 5, 6, 7]
heapSort(A)
print(A)


