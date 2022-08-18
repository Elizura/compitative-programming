# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        if not root: return 0
        if not root.right and not root.left: return 1
        level = 0
        a = deque()
        a.append(root)
        while a:
            for i in range(len(a)):
                b = a.popleft()
                if b.left: a.append(b.left)
                if b.right: a.append(b.right)
            level += 1 
        return level
        