'''
266. Palindrome Permutation

Given a string s, return true if a permutation of the string could form a palindrome.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.
'''

# TC : O(n)
# SC : O(1), since size of set can gow upto character count limit only

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        permCheck = set()
        for i in range(len(s)):
            if s[i] in permCheck:
                permCheck.remove(s[i])
            else:
                permCheck.add(s[i])
        return len(permCheck) <= 1
