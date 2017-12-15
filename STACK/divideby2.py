from STACK.stck import stck

def divideby2(num):
    s = stck()

    while num>0:
        rem = num%2
        s.push(rem)
        num = num//2

    resultString = ""

    while not s.isEmpty():
        resultString = resultString + str(s.pop())

    return resultString

print(divideby2(2))


