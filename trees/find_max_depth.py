# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS method , iterative 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0

        queue = [(root, 1 )] # node , depth till that node 
        res = 0
        while queue :
            current_node, depth = queue.pop(0) # remember queue.pop(0) ...removes first pushed value

            if current_node.left == None and current_node.right == None:
               res = max(res, depth) 
            
            if current_node.left:
                queue.append((current_node.left, depth+1)) # append at last 
                
            if current_node.right:
                queue.append((current_node.right, depth+1))
                
                
        return res
    
    """
    
        3
    9       20
        15      7
    """
    
#################################### DFS recursive 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
   

        def dfs_recursive(curr_node, depth):
            if not curr_node :
                return depth 
            
            
            return max(dfs_recursive(curr_node.left, depth+1), dfs_recursive(curr_node.right, depth+1))
        return dfs_recursive(root, 0)
    
