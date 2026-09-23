# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTreesHelper(self, node1 = None, node2 = None):
        if node1 == None and node2 == None:
            return None
        mergeNode = TreeNode(0, None, None)
        if node1 == None:
            mergeNode.val = node2.val
            mergeNode.left = self.mergeTreesHelper(node2 = node2.left)
            mergeNode.right = self.mergeTreesHelper(node2 = node2.right)
        elif node2 == None:
            mergeNode.val = node1.val
            mergeNode.left = self.mergeTreesHelper(node1 = node1.left)
            mergeNode.right = self.mergeTreesHelper(node1 = node1.right)
        else:
            mergeNode.val = node1.val + node2.val
            mergeNode.left = self.mergeTreesHelper(node1 = node1.left, node2 = node2.left)
            mergeNode.right = self.mergeTreesHelper(node1 = node1.right, node2 = node2.right)
        return mergeNode

    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.mergeTreesHelper(root1, root2)
        return root