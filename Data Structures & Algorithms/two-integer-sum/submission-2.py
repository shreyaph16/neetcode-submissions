class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in result:
                return [result[complement],i]
            result[n] = i 

        return []  