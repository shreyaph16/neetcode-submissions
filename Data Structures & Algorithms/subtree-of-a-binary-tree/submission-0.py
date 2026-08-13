class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # Main function: traverse the main tree
        if not root:
            return False
        if isSameTree(root, subRoot):  # If current subtree matches
            return True
        # Otherwise, check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
            
            


        