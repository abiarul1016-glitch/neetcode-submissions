# semi-brute force solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for index1, num in enumerate(nums):
            compliment = target - num
            if compliment in nums and index1 != nums.index(compliment):
                return sorted([index1, nums.index(compliment)])