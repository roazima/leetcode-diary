#Raya Azima doing this for the millionth time on May1, 2025 until I land a job
from typing import Optional, List
from collections import deque

class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left_w = 0 # create a window with a left and right pointer
        max_sub = 0
        for i in range(len(s)): # loop through the string
            #create a set and if you see the repeated char, remove left pointer & shift the left pointer forward
            while s[i] in seen:  
                seen.remove(s[left_w])
                left_w += 1
            #otherwise, add the char to the set seen and change the right pointer to the
            seen.add(s[i])
            right = i
            max_sub = max(max_sub, right - left_w + 1)
        return max_sub

             

if __name__ == "__main__":
   Solution = Solution()
   s = "aab"
   result = Solution.lengthOfLongestSubstring(s)

   print("Result:", result)
    
