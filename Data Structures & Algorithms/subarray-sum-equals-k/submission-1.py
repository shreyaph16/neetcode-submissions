

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curSum = 0
        prefixSum = {0: 1}

        for n in nums:
            curSum += n
            ans += prefixSum.get(curSum - k, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return ans