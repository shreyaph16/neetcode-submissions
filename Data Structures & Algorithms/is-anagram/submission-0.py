from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)
        if S==T:
            return True
        return False

        