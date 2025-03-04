from typing import *
import math
from collections import deque
import heapq

"""
Find Median in a Data Stream
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
"""
class MedianFinder:
    def __init__(self):
        """
        Initialize the data structures
        """
        # Large and Small Heaps
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Add an element to the small heap (Max Heap)
        # Since Python only implements a MIN HEAP by default, we will multiply all the elements by -1
        heapq.heappush(self.small, -1 * num)

        # Make sure every element in small is <= every num in large
        if (self.small and self.large and 
            ( -1 * self.small[0] ) > self.large[0]):
            val = -1 * heapq.heappop(self.small) # Get the Max element of the small heap
            heapq.heappush(self.large, val) # Move it to the large heap

        # Check if the size of the heaps is uneven
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small) # Get the Max element of the small heap
            heapq.heappush(self.large, val) # Move it to the large heap
        elif len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large) # Get the Min element of the large heap
            heapq.heappush(self.small, val) # Move it to the small heap

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]    # Return the MAX element of the small heap
        
        if len(self.large) > len(self.small):
            return self.large[0]    # Return the MIN element of the large heap
        
        return (-1*self.small[0] + self.large[0]) / 2 

res = MedianFinder()

input1 = [1,2,3]

sol = res.maxPathSum(input1)

print("Solution: ", sol)