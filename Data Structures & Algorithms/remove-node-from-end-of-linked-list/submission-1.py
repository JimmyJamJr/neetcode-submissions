# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for i in range(n):
            first = first.next
        

        dummy = ListNode(0, head)
        second = dummy
        while first:
            first = first.next
            second = second.next

        # second should be at the node right before the one
        # to be removed
        
        second.next = second.next.next
        return dummy.next

        