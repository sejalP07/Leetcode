# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        # Check left child
        if root.left:
            # If left child is a leaf
            if not root.left.left and not root.left.right:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)

        # Traverse right subtree
        ans += self.sumOfLeftLeaves(root.right)

        return ans