import heapq
a = [3,4,5,6,1,2]


def kLarge(k,arr):
    # if k == 1:
    #     return max(arr)
    # max_ = max(arr)
    # new_arr = list(filter(lambda x: x!=max_, arr))
    # # if not new_arr:
    # #     return max_
    # return kLarge(k-1, new_arr)
    # if (k == 1):
    #     return max(arr)
    # else:
    #     m = max(arr)
    #     return(kLarge(k-1, [x for x in arr if x != m]))
    # Bubble Sort implementation
    # for i in range(k):
    #     for j in range(len(arr)-i-1):
    #         if arr[j] > arr[j+1]:
    #             # exchange elements, time consuming
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    # print(arr[len(arr) - k])

    #HeapSort implementation
    heap= []
    for i in arr:
        heapq.heappush(heap,i)

    for _ in range(len(arr) - k):
        heapq.heappop(heap)

    return heapq.heappop(heap)
    #
    # for i in range(k):
    #     for j in range(len(nums) - i - 1):
    #         if nums[j] > nums[j + 1]:
    #                 # exchange elements, time consuming
    #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # print(nums[len(nums) - k])


print(kLarge(2,a))


