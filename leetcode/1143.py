from typing import *

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Dynamic Programming Solution:
        - Build a (n, m) matrix containing that will iteratively build the length
        of the longest common subtring by dividing the problem into subproblems from
        left-to-right.
        '''
        n, m = len(text2), len(text1)
        dp = [([-1] * m) for _ in range(n)] # Set to -1 (not visited)

        def dfs(text1: str, text2: str):
            n = len(text2)
            m = len(text1)

            # Base Cases
            if not text1 or not text2:
                # Reached an edge of the matrix
                return 0
            
            # Check if solution was already visited
            if dp[n-1][m-1] != -1:
                return dp[n-1][m-1]

            # Recursive Formulation
            # If the next character of each string matches -> it will belong 
            # to the largest substring -> increment length of common subsequence
            if text1[0] == text2[0]:
                # Continue calculating largest substring by removing the character from both strings
                dp[n-1][m-1] = 1 + dfs(text1[1:], text2[1:])  # Store solution
                return dp[n-1][m-1]
            
            # Else -> Largest substring either removes text1[0] or text2[0]
            dp[n-1][m-1] = max(
                dfs(text1[1:], text2),
                dfs(text1, text2[1:])
            )   # Store the solution (avoid repeating computation)
            return dp[n-1][m-1]
        
        return dfs(text1, text2)
        

res = Solution()
input1 = ("crabt", "cat")
input2 = ("abcd", "abcd")
input3 = ("abcd", "efgh")
input4 = ("ylqpejqbalahwr", "yrkzavgdmdgtqpg")

sol = res.longestCommonSubsequence(input4[0], input4[1])

print("Solution: ", sol)