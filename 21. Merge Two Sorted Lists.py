# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        res=ListNode(0)
        head=res
        while l1!=None or l2!=None:
            if l1==None:
                res.next=l2
                l2=l2.next
                res=res.next
                continue
            if l2==None:
                res.next=l1
                l1=l1.next
                res=res.next
                continue
            if l1.val<=l2.val:
                res.next=l1
                l1=l1.next
                res=res.next
            else:
                res.next=l2
                l2=l2.next
                res=res.next
        return head.next
    
