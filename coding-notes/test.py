import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root):
        if root is None:
            return "#"
        return str(root.val) + " " + self.serialize(root.left) + " " + self.serialize(root.right)

    def deserialize(self, strs):
        vals = collections.deque(val for val in strs.split())
        return self.build(vals)

    def build(self, vals):
        if not vals:
            return None
        
        val = vals.popleft()
        if val == '#':
            return None
        root = TreeNode(int(val))
        root.left = self.build(vals)
        root.right = self.build(vals)
        return root

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)

    root.right = TreeNode(14)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(16)

    res = Solution().serialize(root)
    print(res)

    root = Solution().deserialize(res)
    
    res = Solution().serialize(root)
    print(res)

