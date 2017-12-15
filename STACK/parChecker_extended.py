from STACK.stck import stck





def parChecker(symbol):
    s = stck()
    balanced = True
    idx = 0
    while idx < len(symbol) and balanced:
        sym = symbol[idx]
        if sym in "([{":
            s.push(sym)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top = s.pop()
                if not matches(top, sym):
                    balanced = False
        idx = idx + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(opener, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(opener) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
