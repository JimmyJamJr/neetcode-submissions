# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2
            
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        i = 0
        while 2 ** i < len(lists):
            for j in range(0, len(lists) - 2 ** i, 2 ** (i + 1)):
                lists[j] = self.mergeLists(lists[j], lists[j + 2 ** i])
            i += 1
                  
        return lists[0]
        
        