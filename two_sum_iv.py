# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()

        def dfs(node):
            if node is None:
                return False
            o = k - node.val
            if o in s:
                return True
            s.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
