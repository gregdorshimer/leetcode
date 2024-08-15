# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            left_depth = 0
        else:
            left_depth = Solution.maxDepth(self, root.left)
        if not root.right:
            right_depth = 0
        else:
            right_depth = Solution.maxDepth(self, root.right)
        return 1 + max(left_depth, right_depth)
