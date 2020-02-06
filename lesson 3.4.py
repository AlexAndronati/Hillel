import heapq

l = [2, -3, 34, 35, 2, -4, -25, 100, 0, 5]
print(l)

heapq.heapify(l)
l = [heapq.heappop(l) for _ in range(len(l))]

print(l)