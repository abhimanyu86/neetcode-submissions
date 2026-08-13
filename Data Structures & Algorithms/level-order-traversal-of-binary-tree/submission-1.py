from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            level = []
            for r in range(len(queue)):
                q = queue.popleft()
                level.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            res.append(level)

        return res