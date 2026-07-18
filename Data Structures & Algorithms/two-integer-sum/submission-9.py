# solution using one-pass hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tracker = {}

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in tracker:
                return [tracker[compliment], index]
            tracker[num] = index