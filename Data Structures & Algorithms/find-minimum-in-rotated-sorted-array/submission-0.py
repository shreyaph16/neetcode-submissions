# Brute Force Solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = float('inf')
        for num in nums:
            if num < minn:
                minn = num
        return minn
 
# Time: O(n)
# Space: O(1)
 
