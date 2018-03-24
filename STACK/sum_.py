def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """

    result = []
    for i in ops:
        if i == 'C':
            result.pop()
        elif i == 'D':
            result.append(result[-1] * 2)
        elif i == '+':
            result.append(result[-1] + result[-2])
        else:
            result.append(int(i))

    return sum(result)

arr = ["5","2","C","D","+"]
ans_ = calPoints(arr)
print(ans_)