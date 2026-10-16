class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            hours = sum(math.ceil(pile / k) for pile in piles)

            if hours <= h:
                right = k
            else:
                left = k + 1

        return left

