from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        m = n//3
        numCount = Counter(nums)
        ans = []

        for num in nums: 
            if numCount[num] > m:
                if num in ans:
                    continue
                ans.append(num)
                

        return ans


        