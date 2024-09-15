# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        parent = None
        current = root
        toberemoved = None
        left = True
        while current:
            if key == current.val:
                toberemoved = current
                break
            elif key < current.val:
                if current.left:
                    if current.left.val == key:
                        parent = current
                        toberemoved = current.left
                        break
                current = current.left
            else:
                if current.right:
                    if current.right.val == key:
                        parent = current
                        toberemoved = current.right
                        left = False
                        break
                current = current.right

        # at end of loop:
        #   current is either the node to be removed, or it is none if not found
        #   toberemoved is the node where toberemoved.val == key
        #   parent is parent of toberemoved, or None if root needs to be removed
        #   left is True if toberemoved is the left child of parent, False if it is the right child

        if not current:
            return root

        # here, current is the node to be removed

        # update parent's pointer:
        # parent will point to the left child of toberemoved, or if None it will point to the right child
        if parent:
            newroot = root
            if toberemoved.left:
                if left:
                    parent.left = toberemoved.left
                else:
                    parent.right = toberemoved.left
            else:
                if left:
                    parent.left = toberemoved.right
                else:
                    parent.right = toberemoved.right
        else:
            if toberemoved.left:
                newroot = toberemoved.left
            else:
                newroot = toberemoved.right

        # attach toberemoved.right at the rightmost child of toberemoved.left
        current2 = toberemoved.left
        while current2:
            if current2.right:
                current2 = current2.right
            else:
                current2.right = toberemoved.right
                break

        return newroot