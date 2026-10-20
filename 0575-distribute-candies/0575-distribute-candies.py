class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        s=len(set(candyType))
        return min(len(candyType)//2, s)
            