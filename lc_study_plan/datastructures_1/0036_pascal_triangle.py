'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

# TC : O(n^2)
# SC : O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        #corner cases
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        triangle = [[1]]
        for i in range(1,numRows):
            row = [1]
            for j in range(1,i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            
            triangle.append(row)
        return triangle
        
