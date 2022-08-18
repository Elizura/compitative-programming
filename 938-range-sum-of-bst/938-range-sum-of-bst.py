# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        a = deque()
        a.append(root)
        while a:
            f = a.popleft()
            if low <= f.val and f.val <= high: ans += f.val
            if f.left: a.append(f.left)
            if f.right: a.append(f.right)            
        return ans
        