# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # TODO note this does not work, but the recurrences are correct
        def zigzags_below(node, left, current_len):
            if not node:
                return current_len
            elif left:
                return zigzags_below(node.right, not left, current_len + 1)
            else:
                return zigzags_below(node.left, not left, current_len + 1)

        if not root:
            return 0
        else:
            return max(max(zigzags_below(root, True, 0),
                           zigzags_below(root, False, 0)),
                       max(Solution.longestZigZag(self, root.left),
                           Solution.longestZigZag(self, root.right)))