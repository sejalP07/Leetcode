class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(1,n+1):
            left=sum(range(1,x+1))
            right=sum(range(x,n+1))
            if left == right:
                return x
        return -1
