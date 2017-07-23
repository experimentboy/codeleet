# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        a = head
        b = head.next
        while 1 == 1:
            if b.next and b.next.next:
                b = b.next.next
            else: return False
            a = a.next
            if a == b: return True
