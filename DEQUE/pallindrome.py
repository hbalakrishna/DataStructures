from DEQUE.deque import deque

def palchecker(inString):
    chardeque = deque()

    for i in inString:
        chardeque.addRear(i)

    checkEqual = True

    while chardeque.size()>1 and checkEqual:
        firstChar = chardeque.removeRear()
        lastChar = chardeque.removeFront()

        if firstChar!=lastChar:
            checkEqual = False

    return checkEqual

print(palchecker("radar"))
print(palchecker("afhjshjfshbba"))