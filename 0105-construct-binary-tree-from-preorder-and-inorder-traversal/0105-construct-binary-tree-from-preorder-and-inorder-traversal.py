# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A preorder traversal is [node, left, right] while an inorder traversal is [left, node, right]
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            # Let the index of preorder[0] in inorder be INDEX
            INDEX = inorder.index(preorder.pop(0))
            # Recursivly create left subtree by passing -> preorder with first element removed and the part of inorder array that lies to the left of INDEX. ->inorder[:INDEX]
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            # Recursivly create right subtree by passing -> the part of inorder array that lies to the right of INDEX. ->inorder[:INDEX]
            root.right = self.buildTree(preorder, inorder[INDEX+1 :])

            return root