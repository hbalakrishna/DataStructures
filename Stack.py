from sys import maxsize

def createStack():
    Stack = []
    return Stack

def isEmpty(Stack):
    return len(Stack)==0

def push(Stack, item):
    Stack.append(item)
    print("pushed to stack {0}".format(item))


def pop(Stack):
    if isEmpty(Stack):
        print("Empty Stack cant be poped")
    else:
        return print(Stack.pop())

stk = createStack()
push(stk, 10)
push(stk, 20)
pop(stk)
pop(stk)
print(isEmpty(stk))



