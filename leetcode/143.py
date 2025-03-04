from typing import *
import math
from utils import DoublyListNode, list_to_linked_list

"""
Reorder Linked List
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""
class Solution:
    def reorderList(self, head: Optional[DoublyListNode]) -> None:
        if not head:
            return

        # Let's create the link to the prev element of the linked list
        # -- Doubly-Linked List
        curr_pt = head
        prev_pt = None
        while curr_pt:
            curr_pt.prev = prev_pt
            prev_pt = curr_pt
            curr_pt = curr_pt.next
            
        # Set the left and right pointers on the Linked List
        right_pt = prev_pt
        left_pt = head

        if left_pt == right_pt:
            return

        # So for each element in the original linked list, we will insert an element in the middle of 2 starting from the end
        # Therefore, we will only do this for len // 2
        while True:
            # Set the next pointer of the right element to the node the left ptr was connected to
            right_pt.next = left_pt.next
            # Set the next point of the left node to the right_ptr
            left_pt.next = right_pt

            # Move the right_pt to the left
            right_pt = right_pt.prev

            # Check if left_pt == right_pt -> break
            # left_pt and left_pt != right_pt and left_pt.val <= right_pt.val
            if left_pt == right_pt:
                left_pt.next.next = None    # Already visited the last element
                return

            # Move the left ptr to the right (2 times)
            for _ in range(2):
                left_pt = left_pt.next
                if left_pt == right_pt:
                    left_pt.next = None
                    return

        # if right_pt.next == right_pt.next:
        #     right_pt.next = None
        # right_pt.next = None

        return # head


res = Solution()

input1 = [2,4,6,8]
input2 = [2,4,6,8,10]
input3 = [1]
input4 = [1,2,3,4,5,6,7]
input5 = [1,2,3,4,5,6,7,8]

head = list_to_linked_list(input5)
# while head != None:
#     print(head.val)
#     head = head.next


res.reorderList(head)
sol = head

# Print Linked list
while sol != None:
    print(sol.val)
    sol = sol.next  # NEXT IS NOT BEING CLEARED IN THE LAST ELEMENT
print("Solution: ", sol)