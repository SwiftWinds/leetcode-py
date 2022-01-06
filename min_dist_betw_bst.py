import itertools
from collections.abc import Iterable
from typing import Optional, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []

        def pairwise(iterable: Iterable) -> Iterable[tuple[Any, Any]]:
            a, b = itertools.tee(iterable)
            next(b, None)
            return zip(a, b)

        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)
        min = float("inf")
        for a, b in pairwise(nums):
            diff = b - a
            if diff < min:
                min = diff
        return min
