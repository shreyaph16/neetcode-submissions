class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        a = 0
        b = n - 1
        mid = (a + b) // 2      # computed once, before a and b start moving

        for i in range(n):
            if n % 2 == 0:
                if i == n // 2:     # halfway for even length, stop
                    break
                s[a], s[b] = s[b], s[a]
                a += 1
                b -= 1

            if n % 2 != 0:
                if i == mid:        # reached the middle element, stop
                    break
                s[a], s[b] = s[b], s[a]
                a += 1
                b -= 1


                