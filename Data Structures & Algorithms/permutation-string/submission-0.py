from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)                   # every window has the same length as s1
        target = Counter(s1)          # letter counts we need to match

        for i in range(len(s2) - k + 1):
            window = s2[i : i + k]    # the k characters starting at i
            if Counter(window) == target:
                return True           # found a permutation, so stop

        return False                  # no window matched