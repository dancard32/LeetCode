# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        sums = []        
        def DepthFirstSearch(node: TreeNode, level: int):
            if level == len(sums):
                sums.append(node.val)
            else:
                sums[level] += node.val
                
            if node.left:
                DepthFirstSearch(node.left, level+1)
            if node.right:
                DepthFirstSearch(node.right, level+1)
                
        DepthFirstSearch(root, 0)
        return sums[-1]
        
        