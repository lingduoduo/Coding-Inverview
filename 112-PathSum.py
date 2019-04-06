# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # First Try
        # if root is None:
        # 	return False
        # if root.left is None and root.right is None and root.val == sum:
        # 	return True
        # if self.hasPathSum(root.left, sum-root.val):
        # 	return True
        # if self.hasPathSum(root.right, sum-root.val):
        # 	return True
        # return False

        # Second Try
        # if not root:
        #     return False
        # if not root.left and not root.right and root.val == sum:
        #     return True
        # left = right = False
        # if root.left:
        #     left = self.hasPathSum(root.left, sum-root.val)
        # if root.right:
        #     right = self.hasPathSum(root.right, sum-root.val)
        # return left or right

        # Third Try
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        return self.hasPathSum(
            root.left,
            sum -
            root.val) or self.hasPathSum(
            root.right,
            sum -
            root.val)
