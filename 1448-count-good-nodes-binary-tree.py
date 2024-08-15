# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def goodNodesRecur(rt, mx):
            if not rt:
                return 0
            leftGoodNodes = goodNodesRecur(rt.left, max(mx, rt.val))
            rightGoodNodes = goodNodesRecur(rt.right, max(mx, rt.val))
            return leftGoodNodes + rightGoodNodes + (rt.val >= mx)
        return goodNodesRecur(root, root.val)
