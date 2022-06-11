# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# modifies the linked list !!!!
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        pointer=head
        while pointer.next != None:
            if type(pointer.next.val) != int:
                return True
            pointer.val="GG"
            pointer=pointer.next
        return False
      
