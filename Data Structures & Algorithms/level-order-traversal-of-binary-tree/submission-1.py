# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        Q = deque([root])
       

        while Q:
            level = []
            for _ in range(len(Q)):
                node = Q.popleft()
                level.append(node.val)

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

            result.append(level)


        return result
                       