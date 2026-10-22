
import heapq

class Solution:
    def smallestRange(self, nums):
        heap = []
        maximum = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            maximum = max(maximum, nums[i][0])

        start, end = heap[0][0], maximum

        while True:
            minimum, i, j = heapq.heappop(heap)

            if maximum - minimum < end - start:
                start, end = minimum, maximum

            if j + 1 == len(nums[i]):
                break

            value = nums[i][j + 1]
            heapq.heappush(heap, (value, i, j + 1))
            maximum = max(maximum, value)

        return [start, end]
