class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        result = float("inf")
        currSum = 0

        for r in range(len(nums)):
            currSum+=nums[r]
            while currSum >= target:
                result = min(r-l+1, result)
                currSum -= nums[l]
                l+=1

        return 0 if result == float("inf") else result