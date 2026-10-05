class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = sorted(set(nums))
        nums[:len(ans)] = ans

        return len(ans)

       