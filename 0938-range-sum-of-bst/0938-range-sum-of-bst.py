# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sums = 0
        def dfs(tree):
            if high >= tree.val >= low:
                self.sums += tree.val
            
            if tree.right is not None:
                dfs(tree.right)
                
            if tree.left is not None:
                dfs(tree.left)
        dfs(root)
        return self.sums