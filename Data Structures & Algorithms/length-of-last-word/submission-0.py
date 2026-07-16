class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Slist = s.split()
        n = len(Slist)
        return len(Slist[n-1])
       

        