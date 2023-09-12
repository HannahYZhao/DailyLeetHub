/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
 // Breadth First Search
 // Time complexity: O(n)
 // Space complexity: O(n)
var levelOrder = function(root) {
    // Initialize a queue to store the nodes on the same level & add root in it...
    let q = [root]
    // Create an array list to store the output result...
    output = []
    // Traverse a loop. until the queue becomes empty...
    while (q[0]) {
        // Denote the number of elements on that level...
        let size = q.length
        // A temporary list to store all the left and right child for all the node in the level...
        temp = []
        for (let i = 0; i < size; i++) {
            let node = q.shift()
            // Store the value of node to temp...
            temp.push(node.val)
            // Store all the nodes of next level...
            // Add left and right child if they are not None...
            if (node.left) q.push(node.left)
            if (node.right) q.push(node.right)
        }
        // Add the temp to output result...
        output.push(temp)
    }
    return output       // Return the output result...
};