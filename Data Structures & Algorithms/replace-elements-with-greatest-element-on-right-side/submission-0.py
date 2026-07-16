class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = []

        for i in range(0, n):
            if i == n - 1:
                output.append(-1)
            else:
                output.append(max(arr[i+1:]))

        return output
        