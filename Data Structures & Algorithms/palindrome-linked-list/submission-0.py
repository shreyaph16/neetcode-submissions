# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
            n+=1
        
        l = 0
        r = n-1

        while l<r:
            if vals[l]!=vals[r]:
                return False
            l+=1
            r-=1

        return True

