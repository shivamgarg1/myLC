class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min_val = root.val
        while root:
            min_val = min(min_val, root.val, key = lambda x : (abs(x - target), x))
            root = root.left if root.val > target else root.right
        return min_val