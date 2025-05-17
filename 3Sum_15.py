# R Azima
# Given an integer areray nums, return all the triplets such that i != j, i !=k, & j!= k
# - and nums[i]+nums[j]+nums[k] == 0
# Time Complexity: O(n^2)
# Outer loop over elements: O(n), inner two pointer search: O(n) total = o(n^2)
# Space Complexity: O(1)
# only returning results, and not using extra space (aka hash sets)
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting will make this very smoother
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #create two pointers for nums[j] & nums[k]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                #if we need a bigger number
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])

                    # need to skip duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
            
                    j += 1
                    k -= 1

        return result 

if __name__ == "__main__":
    test_cases = [
        ([-1,0,1,2,-1,-4]),
        ([0,1,1]),
        ([0,0,0])   
    ]

    solver = Solution()
    for nums in test_cases:
        result = solver.threeSum(nums)
        print(f"Input: '{nums}'' → Output: {result}")
