# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        turtle = head
        rabbit = head.next

        while rabbit is not None and rabbit.next is not None:
            turtle = turtle.next
            rabbit = rabbit.next.next

        # turtle at start of second half of array
        second_half = turtle.next
        turtle.next = None

        # reverse second half of array
        prev_node = None
        while second_half is not None:
            next_node = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = next_node
        
        reversed_head = prev_node

        while reversed_head:
            head_next = head.next
            reversed_next = reversed_head.next

            head.next = reversed_head
            reversed_head.next = head_next

            head = head_next
            reversed_head = reversed_next
        

            
        

        



