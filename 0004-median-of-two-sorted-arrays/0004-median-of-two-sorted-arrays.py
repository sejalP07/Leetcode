class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:

            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            leftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            rightX = float('inf') if partitionX == m else nums1[partitionX]

            leftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            rightY = float('inf') if partitionY == n else nums2[partitionY]

            if leftX <= rightY and leftY <= rightX:

                if (m + n) % 2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY)) / 2

                return max(leftX, leftY)

            elif leftX > rightY:
                high = partitionX - 1

            else:
                low = partitionX + 1