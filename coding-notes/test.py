class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def convertTree(self, root):
        self.prev = None
        self.inOrder(root)
        return root

    def inOrder(self, root):
        if root is None: 
            return None 

        self.inOrder(root.left)

        root.left = self.prev
        if self.prev:
            self.prev.right = root 
        self.prev = root

        self.inOrder(root.right)


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(14)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(16)

    res = Solution().convertTree(root)
    p = res
    print(p.val)
    while p.right:
        print(p.right.val)
        p = p.right

    while p.left:
        print(p.val)
        p = p.left





