from STACK.stck import stck

def parChecker(symbol):
    s = stck()
    balanced = True
    idx = 0
    while idx <len(symbol) and balanced:
        sym = symbol[idx]
        if sym == '(':
            s.push(sym)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        idx = idx + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False



print(parChecker('(())'))
print(parChecker('())'))


