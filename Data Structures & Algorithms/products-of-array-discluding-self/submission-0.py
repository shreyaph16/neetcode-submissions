class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        left, right = 0, n - 1
        left_product, right_product = 1, 1

        while left < n:
            output[left] *= left_product
            output[right] *= right_product

            left_product *= nums[left]
            right_product *= nums[right]

            left += 1
            right -= 1

        return output




            


        