# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev_node = None
        while head is not None:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node
