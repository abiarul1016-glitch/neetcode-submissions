# semi-brute force solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # iterates through each num in the list, identifying whether the complement to the current num to sum to the target exists
        for index1, num in enumerate(nums):
            compliment = target - num

            # if so, and their indexes are not the same, it returns a sorted list
            if compliment in nums:
                index2 = nums.index(compliment)

                if index1 != index2:
                    return sorted([index1, index2])