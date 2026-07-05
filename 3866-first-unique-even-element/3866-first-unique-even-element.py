class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}

        # Count frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Find the first even number with frequency 1
        for num in nums:
            if num % 2 == 0 and freq[num] == 1:
                return num

        return -1
        