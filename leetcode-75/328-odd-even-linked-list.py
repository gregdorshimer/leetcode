# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        endofeven = head
        firstodd = head.next
        endofodd = head.next
        current = head
        flag = True
        while current.next:
            current = current.next
            if flag:
                endofeven.next = current.next
                if current.next:
                    endofeven = current.next
                else:
                    break
                flag = False
            else:
                endofodd.next = current.next
                if current.next:
                    endofodd = current.next
                else:
                    break
                flag = True
        endofeven.next = firstodd
        return head


