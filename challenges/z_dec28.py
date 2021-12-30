
###
28 Dec 2021

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        print(head)
        result = head
        counter = 1
        current_node = head
        # Iterate once to count the nodes
        while current_node.next != None:
            counter+=1
            current_node = current_node.next
        if counter==1:
            return result
        if counter % 2 == 0:
            for i in range(0,counter//2):
                result = result.next
            return result
        else:
            for i in range(0,counter//2):
                result = result.next
            return result


LEARNED: 
	You can trade memory for speed and ease.
	Making a list object and appending each "next" node allows you to get back to the half way point fast

NOTE: 
	[]: means list
		list is mutable, unlike strings
	You can reference the last item in a list with var[-1]
	You can append to a list with .append()
	len() returns length
	// is floor division
	% is modulo
	assign more than one at a time: var1 = var2 = 2
	
