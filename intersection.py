from typing import Optional, List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # Definition for singly-linked list.
# def build_linked_list(values: List[int]) -> Optional[ListNode]:
#     dummy = ListNode()
#     current = dummy
#     for v in values:
#         current.next = ListNode(v)
#         current = current.next
#     return dummy.next

# def print_linked_list(head: Optional[ListNode]) -> None:
#     vals = []
#     while head:
#         vals.append(head.val)
#         head = head.next
#     print("Linked List:", vals)

from collections import deque

class Solution:
   def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_set = set()
        full_set = set()
        for i in range(len(nums1)):
           first_set.add(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] in first_set:
                full_set.add(nums2[j])
        return full_set
            
        

if __name__ == "__main__":
   Solution = Solution()
   nums1 = [4,9,5]
   nums2 = [9,4,9,8,4]
   result = Solution.intersection(nums1 ,nums2)

   print("Result:", result)
    
