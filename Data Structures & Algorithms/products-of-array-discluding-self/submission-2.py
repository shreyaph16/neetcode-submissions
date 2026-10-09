class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n

        l = 0
        r = n-1

        LeftProduct = 1
        RightProduct = 1

        

        while l<n:
            output[l]*=LeftProduct
            output[r]*=RightProduct

        
            LeftProduct*=nums[l]
            RightProduct*=nums[r]

            l+=1
            r-=1

        return output