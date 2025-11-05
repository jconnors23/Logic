# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1 2 3  
# 4 5 6 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 🌟 DUMMY NODE BOILERPLATE 🌟
        # 1. Create the dummy (prehead) node.
        dummy = ListNode()
        
        # 2. 'tail' pointer is what we use to build the new list.
        tail = dummy
        
        # Main loop: Iterate while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                # 1. Splice the node from list1
                tail.next = list1
                # 2. Advance the pointer on list1
                list1 = list1.next  # type: ignore
            else:
                # 1. Splice the node from list2
                tail.next = list2
                # 2. Advance the pointer on list2
                list2 = list2.next  # type: ignore
                
            # 3. Always advance the tail pointer to the newly added node
            tail = tail.next
            
        # Handle the remainder
        # Since the remaining part of a non-null list is already sorted,
        # we can just attach it to the end of the merged list.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # 🌟 RETURN STATEMENT 🌟
        # The head of the merged list is the node after the dummy.
        return dummy.next
        


        