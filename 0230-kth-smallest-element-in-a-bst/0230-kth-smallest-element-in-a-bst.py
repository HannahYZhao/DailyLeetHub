# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BST
class Solution(object):
    # k, the position of the smallest element we want to find
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        # Calls the helper method to perform an in-order traversal of the tree. This traversal visits the nodes of the BST in ascending order.
        self.helper(root, count)
        return count[k-1]
    # Recursively calls the helper method on the left child of the current node. This explores all the nodes in the left subtree (which are smaller than the current node).
    def helper(self, node, count):
        if not node:
            return
        
        self.helper(node.left, count)
        # Adds the value of the current node to the count list. In an in-order traversal, this step occurs after visiting the left subtree and before visiting the right subtree.
        count.append(node.val)
        self.helper(node.right, count)
