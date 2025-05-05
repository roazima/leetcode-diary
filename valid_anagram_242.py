# Author: Raya Azima
# Problem: Valid Anagram
# Date: May 5, 2025 — practicing until I land the job!
# I used Counter because what counter does is same as : hash_s[char] = hash_s.get(char, 0) + 1
# Time Complexity: o(n+m) = O(k) n = len(s) m = len(t) 
# Space Complexity: o(n+m)
# If the input might contain Unicode characters that should
# -be normalized aka, accented letters treated the same as base characters;Would use Python’s unicodedata library
# - to normalize the strings first before comparing.
from collections import Counter

class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)
      
if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("listen", "silent"),
        ("aabb", "bbaa"),
        ("hello", "world")
    ]

    solver = Solution()
    for s, t in test_cases:
        result = solver.isAnagram(s, t)
        print(f"Input: '{s}', '{t}' → Output: {result}")
