from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked(arr: list) -> Optional[ListNode]:
    """Build a linked list from a Python list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_to_list(head: Optional[ListNode]) -> list:
    """Convert a linked list to a Python list (for comparing results)."""
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None: return list1
        if list1 is not None and list2 is None: return list1
        if list1 is None and list2 is not None: return list2

        curr1, curr2 = list1, list2
        dummy = ListNode(0)
        tail = dummy
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        if curr1 is not None and curr2 is None:
            tail.next = curr1
        if curr1 is None and curr2 is not None:
            tail.next = curr2
        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([], [0]), [0]),
        (([0], []), [0]),
    ]

    for (arr1, arr2), expected in test_cases:
        list1 = list_to_linked(arr1)
        list2 = list_to_linked(arr2)
        result = sol.mergeTwoLists(list1, list2)
        actual = linked_to_list(result)
        if actual == expected:
            print(f"Pass | {arr1} + {arr2} -> {actual}")
        else:
            print(f"Fail | {arr1} + {arr2} -> Expected {expected}, Got {actual}")