class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # If it's a leaf node, check if the remaining sum equals its value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recur on left and right subtree with reduced sum
        remaining_sum = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))