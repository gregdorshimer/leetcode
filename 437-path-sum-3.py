# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0

        def paths_from_root_recur(node, val_above):
            if not node:
                return 0
            elif val_above + node.val == targetSum:
                return (1 + paths_from_root_recur(node.left, val_above + node.val) +
                        paths_from_root_recur(node.right, val_above + node.val))
            else:
                return (paths_from_root_recur(node.left, val_above + node.val) +
                        paths_from_root_recur(node.right, val_above + node.val))

        return (paths_from_root_recur(root, 0) + Solution.pathSum(self, root.left, targetSum) +
                Solution.pathSum(self, root.right, targetSum))
