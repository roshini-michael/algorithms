'''
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''

# TC : O(n)
# SC : O(1)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # return str(int(num1) + int(num2))
        
        x1 = 0
        x2 = 0
        for i in num1:
            x1 = x1 * 10 + (ord(i) - ord('0'))
        for j in num2:
            x2 = x2 * 10 + (ord(j) - ord('0'))
        
        return str(x1 + x2)
