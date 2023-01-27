import heapq
# numbers = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

N = int(input())
heap = []

# 순회하면서 
for _ in range(N):
    n = int(input())
    # 0이 아니면 heappush 
    if n != 0:
        heapq.heappush(heap, n)
    # 0이면 heappop
    else:
        if heap: # if len(heap) != 0
            print(heapq.heappop(heap))
        else:
            print(0)