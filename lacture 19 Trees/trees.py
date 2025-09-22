class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def print_pre_order(root):
    if root is None:
        print(-1)