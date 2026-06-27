from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = Counter(nums)
        for n in numCount:
            if numCount[n]>=2:
                return True
        return False
       