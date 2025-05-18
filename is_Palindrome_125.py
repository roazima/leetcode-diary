# R Azima
# Leetcode 

# Time Complexity: 
# 

# Space Complexity: 
# 

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
       left ,right = 0, len(s) - 1
       
       while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                    return False
            left +=1
            right -=1

       return True    
       

if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama"),
        ("race a car"),
        (" ")   
    ]

    solver = Solution()
    for s in test_cases:
        result = solver.isPalindrome(s)
        print(f"Input: '{s}' → Output: {result}")

    