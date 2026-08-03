class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow1 = slow2 = dummy

        for _ in range(n):
            slow2 = slow2.next

        while slow2.next:
            slow1 = slow1.next
            slow2 = slow2.next

        slow1.next = slow1.next.next
        return dummy.next