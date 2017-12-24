from QUEUE.queue import Queue

def hotPotato(namelist, num):
    playerQueue = Queue()

    for name in namelist:
        playerQueue.enqueue(name)

    while playerQueue.size()>1:
        for i in range(num):
            playerQueue.enqueue(playerQueue.dequeue())

        playerQueue.dequeue()

    return playerQueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
