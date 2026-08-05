class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(node, res):
            if not node:
                res.append(None)
                return
            res.append(node.val)
            preorder(node.left, res)
            preorder(node.right, res)

        p_res, q_res = [], []
        preorder(p, p_res)
        preorder(q, q_res)
        return p_res == q_res