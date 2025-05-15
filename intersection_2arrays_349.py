# R Azima
# Leetcode #349 : Given two integer arrays nums1 and nums2, 
# - Return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
# I looped through the second array. For each element, I checked if it exists in the first array and if it has not already been added to the result set.
# - If both conditions are met, I added it to the result.
# Time Complexity: O(n * m)
# - For each element in the second array (n), I check for membership in the first array (which is O(m) if it's a list).
# - Worst-case time complexity is O(n * m).
# - This could be optimized to O(n + m) by converting one of the arrays to a set first for constant-time lookups.
# Space Complexity: O(n + m)
# Worst case, we store all elements from both arrays in memory (as sets or temporary structures).

from typing import List

class Solution:
   def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        full_set = []
      #   for i in range(len(nums1)):
      #      first_set.add(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] in nums1:
               if nums2[j] not in full_set:
                full_set.append(nums2[j])
        return full_set
            
        

if __name__ == "__main__":
   Solution = Solution()
   nums1 = [4,9,5]
   nums2 = [9,4,9,8,4]
   result = Solution.intersection(nums1 ,nums2)

   print("Result:", result)
    
