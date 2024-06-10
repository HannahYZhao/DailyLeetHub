# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head==None or head.next == None or head.next.next == None:
            return head
        odd=ListNode(head.val)
        even=ListNode(head.next.val)
        oddPtr = odd
        evenPtr = even
        ptr = head.next.next
        count=2
        while ptr!= None:
            count+=1
            if count%2 == 0:
                n = ListNode(ptr.val)
                evenPtr.next=n
                evenPtr=evenPtr.next
            else:
                n = ListNode(ptr.val)
                oddPtr.next=n
                oddPtr=oddPtr.next
            if ptr.next == None:
                oddPtr.next=even
            ptr=ptr.next
        return odd
