# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # push digits so we can read them back from least significant
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        head = None
        carry = 0
        while s1 or s2 or carry:              # keep going while there's a final carry
            total = carry
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()             # an empty stack contributes 0
            carry, digit = divmod(total, 10)
            head = ListNode(digit, head)      # prepend: new node points at the old head
        return head
        