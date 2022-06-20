# Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return new_head
      
# Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head=None
        while head:
            temp=head.next
            head.next=new_head
            new_head=head
            head=temp
            
        return new_head
