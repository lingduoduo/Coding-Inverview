# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    #     result = []
    #     self.DFS(root, result, 0)
    #     return result[::-1]
    #
    # def DFS(self, root, result, level):
    #     if not root: return
    #     if level >= len(result):
    #         result.append([])
    #     result[level].append(root.val)
    #     self.DFS(root.left, res, level + 1)
    #     self.DFS(root.right, res, level + 1)
    
    
