class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1

        while a <= b:
            m = (a + b) // 2
            if nums[m] == target:
                return m              # found it, return the index
            elif nums[m] > target:
                b = m - 1             # target is in the left half
            else:
                a = m + 1             # target is in the right half

        return a                      # not found: a is the insert position