from queue import PriorityQueue

cards = PriorityQueue()
answer = 0
N = int(input())
for i in range(N):
    cards.put(int(input()))

while cards.qsize() > 1:
    c1 = cards.get()
    c2 = cards.get()
    answer += c1 + c2
    cards.put(c1 + c2)

print(answer)