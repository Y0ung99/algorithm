import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a + b
    heapq.heappush(heap, a + b)

print(result)