from typing import *

'''
Container With Most Water
You are given an integer array heights where heights[i] represents the height of the i-th bar

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
'''
class Solution:
    '''
    Greedy Algorithm with Sliding window (left and right pointers)

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_capacity = 0    # Store the max. found capacity
        while l < r:
            min_height = min(heights[l], heights[r])
            width = r-l

            # Calculate the current capacity
            cur_capacity = width * min_height
            # Update the max capacity
            max_capacity = max(max_capacity, cur_capacity)

            # Greedy approach: Increment the left pointer if height[left] <= height[right].
            # Otherwise, Decrement the right pointer
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_capacity
    

res = Solution()
input1 = [1,7,2,5,4,7,3,6]
input2 = [2,2,2]

sol = res.maxArea(input1)

print("Solution: ", sol)