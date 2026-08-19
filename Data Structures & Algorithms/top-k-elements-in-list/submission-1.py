from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # lista = []
        # while k > 0 and nums:
        #     most_frequent = max(set(nums), key=nums.count)
        #     lista.append(most_frequent)
        #     nums = [value for value in nums if value != most_frequent]
        #     k-=1    

                return [num for num, _ in Counter(nums).most_common(k)]

