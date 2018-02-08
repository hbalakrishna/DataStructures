from functools import reduce


def atoz(ip):
    # i = 1
    # d = {}
    # for one in range(65,91):
    #     d[chr(one)] = i
    #     i+=1
    #
    # sum_1 = 0
    # if len(ip)==1:
    #     return d[ip]
    # else:
    #     for i in ip:
    #         sum_1 = sum_1 + d[i]
    #     return sum_1
    a = []
    for c in list(ip):
        a.append(ord(c) - 64)

    return(reduce(lambda x, y: x * 26 + y, [i for i in a]))



atoz('AAA')