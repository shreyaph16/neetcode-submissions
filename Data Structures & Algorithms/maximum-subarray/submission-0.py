class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        Sum = 0
        

        for i in range(0,n):
            Sum+=nums[i]
            maxSum = max(maxSum, Sum)
            if Sum < 0:
                Sum = 0

        return maxSum
            