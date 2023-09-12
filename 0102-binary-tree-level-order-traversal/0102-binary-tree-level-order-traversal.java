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
 // Time complexity: O(n)
 // Space complesity: O(n)
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        // Declare a Queue named q that will be used for level-by-level traversal of the binary tree...
        Queue<TreeNode> q = new LinkedList<>();
        // Declare a List of Lists of Integers named finalAns to store the final result...
        List<List<Integer>> finalAns = new ArrayList<List<Integer>>();
        // Check if the root of the binary tree is null. If it is, return the empty list of lists...
        if(root==null) {
            return finalAns;
        }
        // Add the root node of the binary tree to the queue...
        q.add(root);
        while(!q.isEmpty()) {
            // Get the size of the current level of the queue...
            int levels = q.size();
            // Create a new list to store the values of the current level...
            List<Integer> subLevels = new ArrayList<>();
            // For each node in the current level of the queue, add its left and right children (if they exist) to the end of the queue and add its value to the list of values for the current level...
            for(int i=0;i<levels;i++) {
                if(q.peek().left!=null) {
                    q.add(q.peek().left);
                }
                if(q.peek().right!=null) {
                    q.add(q.peek().right);
                }
                subLevels.add(q.remove().val);
            }
            // Add the list of values for the current level to the final result list...
            finalAns.add(subLevels);
        }
        return finalAns;
    }
}