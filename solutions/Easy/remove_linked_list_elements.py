# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# small space #O(n)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        while head:
            if head.val == val:
                head=head.next
            else:
                break
                
        pntr=head
        
        while pntr:
            if pntr.val != val:
                prev=pntr
                pntr=pntr.next
            else:
                prev.next=pntr.next
                pntr=pntr.next
        return head
