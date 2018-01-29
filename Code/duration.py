def f(timeSeries, duration):
    # a = set()
    diff1 = 0
    for i in range(len(timeSeries) - 1):
        if timeSeries[i+1] - timeSeries[i] > duration:
            diff1 += duration
        else:
            diff1 += timeSeries[i+1] - timeSeries[i]

    return diff1 + duration if timeSeries else 0
    # for i in ts:
    #     for j in range(1, d + 1):
    #         a.add(i + j)
    #
    # n = len(set((i + j) for i in ts for j in range(1, d + 1)))
    #
    # return n
    # ans = 0
    # for i in range(len(timeSeries) - 1):
    #     ans += min(duration, timeSeries[i + 1] - timeSeries[i])
    # return ans + duration if timeSeries else 0

print(f([1,4], 2))


