# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head

        while turtle is not None and rabbit is not None:
            if rabbit.next is None:
                return False
            
            rabbit = rabbit.next.next
            turtle = turtle.next

            if rabbit == turtle:
                return True

        return False