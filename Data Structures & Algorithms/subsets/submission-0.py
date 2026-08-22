class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        subset =[]

        def subsetFind(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])

            subsetFind(i+1)

            subset.pop()
            subsetFind(i+1)
        
        subsetFind(0)

        return res