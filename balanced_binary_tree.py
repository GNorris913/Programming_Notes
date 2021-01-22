# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.csym(root, root)
    
    def csym(self, t1,t2):
        if t1==None and t2 == None: return True;
        if t1==None or t2== None: return False;
        x = self.csym(t1.right, t2.left)
        y = self.csym(t1.left, t2.right)
        z = t1.val == t2.val
        if x and y and z: return True
        else:
            return False
        
        
    """
      node: check left: check right:
      return symmetric
      *not mentioned, left and right values have to be the same*
    
    """    
   
