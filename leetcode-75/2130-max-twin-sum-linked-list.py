# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        nums = [head.val]
        current = head
        while current.next:
            nums.append(current.next.val)
            current = current.next
        current_max = 0
        for i in range(int(len(nums)/2)):
            current_max = max(current_max, nums[i] + nums[len(nums) - i - 1])
        return current_max