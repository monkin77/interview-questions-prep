from typing import *
import math
from utils import ListNode, list_to_linked_list

"""
Merge Two Sorted Linked Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        if not list1:
            return list2
        if not list2:
            return list1

        curr_l1 = list1
        curr_l2 = list2
        if list1.val <= list2.val:
            head = ListNode(val=list1.val)
            curr_l1 = curr_l1.next
        else:
            head = ListNode(val=list2.val)
            curr_l2 = curr_l2.next

        prev_node: ListNode = head
        curr_node: ListNode = None
        while True:
            if curr_l1 is None:
                # Append the remaining of L2 (If l2 is also none, appends None)
                curr_node = curr_l2
                prev_node.next = curr_node
                break
            if curr_l2 is None:
                # Append the remaining of L1
                curr_node = curr_l1
                prev_node.next = curr_node
                break

            if curr_l1.val <= curr_l2.val:
                curr_node = ListNode(val = curr_l1.val)
                prev_node.next = curr_node
                prev_node = curr_node
                curr_l1 = curr_l1.next  # Go to the next element of L1
            else:
                curr_node = ListNode(val = curr_l2.val)
                prev_node.next = curr_node
                prev_node = curr_node
                curr_l2 = curr_l2.next  # Go to the next element of L2

        
        return head


res = Solution()

input1 = ([1,2,4], [1,3,5])
input2 = ([], [1, 2])
input3 = ([], [])

heads = (list_to_linked_list(input1[0]), list_to_linked_list(input1[1]))
# while head != None:
#     print(head.val)
#     head = head.next


sol = res.reverseList(heads[0], heads[1])
print("Solution: ", sol)