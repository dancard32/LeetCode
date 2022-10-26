# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root)
        return self.values[k - 1]
    def dfs(self, node):
        if node is None:
            return        

        self.dfs(node.left)
        self.values.append(node.val)
        self.dfs(node.right)