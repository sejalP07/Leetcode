class Solution(object):
    def lastStoneWeight(self, stones):
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)   # Largest
            second = -heapq.heappop(max_heap)  # Second largest

            if first != second:
                heapq.heappush(max_heap, -(first - second))

        if max_heap:
            return -max_heap[0]
        return 0