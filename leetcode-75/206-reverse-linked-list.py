# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        current = head
        prev = None
        while current.next:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        return current
