# R Azima
# Leetcode #1 Two Sum : Given an array of int and integer target, return indices of the two numbers such that they add up to target
# Created a hash map to store values from the array as keys and their indices as values.
# - As I iterate through the array,I calculate the complement of each element (target - current value).
# - If the complement exists in the hash map, I return the index of the complement and the current index.

# Time Complexity: O(n)
# - Traverse the array once, and hash map operations (insert + lookup) are O(1) on average.

# Space Complexity: O(n)
# - In the worst case, we store every element in the array in the hash map.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash_seen = {}

       for i,n in enumerate(nums):
            compliment = target - n
            if compliment in hash_seen:
                return [hash_seen[compliment], i]
            hash_seen[n] = i     

if __name__ == "__main__":
    test_cases = [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([3,3], 6)   
    ]

    solver = Solution()
    for nums, target in test_cases:
        result = solver.twoSum(nums, target)
        print(f"Input: '{nums}', '{target}' → Output: {result}")

    