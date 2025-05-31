from typing import *
import math
from utils import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes: set = set()

        while head != None:
            if head in visited_nodes:
                # Found a cycle
                return True

            visited_nodes.add(head)
            head = head.next
        
        return False
        