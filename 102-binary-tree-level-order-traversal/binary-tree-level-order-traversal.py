# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)

        def level_travers(node, level):

            if node:
                store[level].append(node.val)

                level_travers(node.left, level + 1)
                level_travers(node.right, level + 1)
        
        level_travers(root, 0)

        res = sorted(store.keys())
        ans = [store[key] for key in res]

        return ans



        