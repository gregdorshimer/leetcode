# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lom = None
        right = head
        if right.next:
            right = right.next
        else:
            return None # the base case is: deleteMiddle([1]) -> []
        while True:
            if right.next:
                right = right.next
                if right.next:
                    lom = lom.next
                    right = right.next
                else:
                    lom.next = lom.next.next
                    break
            else:
                lom.next = lom.next.next
                break
        return head

