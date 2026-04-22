class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            # Current node must be strictly within bounds
            if not (low < node.val < high):
                return False
            
            # Left subtree: update upper bound
            # Right subtree: update lower bound
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)