# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        left_leaves = []
        left_nodes = [root1]
        right_leaves = []
        right_nodes = [root2]

        while len(left_nodes) != 0:
            node = left_nodes.pop()
            if not node.left and not node.right:
                left_leaves.append(node)
            if node.left:
                left_nodes.append(node.left)
            if node.right:
                left_nodes.append(node.right)
        while len(right_nodes) != 0:
            node = right_nodes.pop()
            if not node.left and not node.right:
                right_leaves.append(node)
            if node.left:
                right_nodes.append(node.left)
            if node.right:
                right_nodes.append(node.right)
        return left_leaves == right_leaves
