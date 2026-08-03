# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set()
        if head==None:
            return False
        while head.next!=None:
            x=head.val
            if x in seen:
                return True
            seen.add(x)
            head=head.next
        return False
         