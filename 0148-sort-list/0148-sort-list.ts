/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function sortList(head: ListNode | null): ListNode | null {
    if(!head)
        return null;
    
    //Push all nodes of linked list into the array along with their node value
    let array = [];
    while(head) {
        array.push([head, head.val]);
        head = head.next;
    }
    
    //Sort the Array in ascending order of the node values
    array.sort((a,b) => {
        return a[1]-b[1];
    });
    
    // Link each node of the array
    for (let iter = 0; iter < array.length; iter++) {
        if (iter + 1 >= array.length)
            array[iter][0].next = null;
        else
            array[iter][0].next = array[iter+1][0];
    }
    
    //return 1st node as it is the new head
    return array[0][0];
};