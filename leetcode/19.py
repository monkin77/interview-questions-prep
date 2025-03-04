from typing import *
import math
from utils import ListNode, list_to_linked_list

"""
Remove Node From End of Linked List
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_node = head
        # Get the length of the list
        len = 0
        while curr_node:
            curr_node = curr_node.next
            len += 1

        # index of node to remove
        remove_idx = len - n

        curr_node = head
        prev_node = None
        for _ in range(remove_idx):
            prev_node = curr_node
            curr_node = curr_node.next
        
        next_node = curr_node.next
        if prev_node:
            prev_node.next = next_node
        else:
            return next_node
        
        return head


res = Solution()

input1 = ([1,2,3,4], 2)
input2 = ([1], 1)
input3 = ([1,2], 2)


head = list_to_linked_list(input3[0])
# while head != None:
#     print(head.val)
#     head = head.next


sol = res.removeNthFromEnd(head, input3[1])

# Print Linked list
while sol != None:
    print(sol.val)
    sol = sol.next  # NEXT IS NOT BEING CLEARED IN THE LAST ELEMENT
# print("Solution: ", sol)