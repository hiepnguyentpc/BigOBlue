
import queue
deck = queue.Queue()

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(1, n+1):
        deck.put(i)

    discarded = []

    while deck.qsize() >= 2:
        discarded.append(deck.get())
        deck.put(deck.get())

    print('Discarded cards: ' if discarded else 'Discarded cards:', end = '')
    print(*discarded, sep=', ')
    print('Remaining card: {}'.format(deck.get()))
