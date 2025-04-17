# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        q = deque()
        
        if root:
            q.append(root)

        while q:

            n = len(q)
            maxx = max(q, key = lambda x: x.val)
            ans.append(maxx.val)

            for _ in range(n):
                node = q.popleft()

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)
        
        return ans



        