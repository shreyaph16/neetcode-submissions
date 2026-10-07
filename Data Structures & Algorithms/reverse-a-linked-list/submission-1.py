# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        a = None
        b = head

        while b:
            temp = b.next #temp var goes to c, saves nxt node
            b.next = a #var a moves to b 
            a = b 
            b = temp 

        return a

