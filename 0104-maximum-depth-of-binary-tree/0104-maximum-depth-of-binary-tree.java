/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        // If the subtree is empty, root is NULL, return depth is 0...
        if(root == null)    return 0;
        // If root is not NULL, call the same function recursively for its left child and right child...
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);
        // When the two child function return its depth...
        // Pick the maxium out of these two subtrees and return this value after adding 1 to it...
        // Adding 1 is the current node which is the parant of the two subtrees...
        return Math.max(leftDepth, rightDepth) + 1;
    }
}