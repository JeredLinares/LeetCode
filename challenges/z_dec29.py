

###
29 Dec 2021
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.




"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        if root.left == None:
            return root
        
        still_working = True
        
        
        bfs = [root]
        while still_working:
            this_level = []
            for i in range(0,len(bfs)):
                this_level.append(bfs[i].left)
                this_level.append(bfs[i].right)
            
            for i in range(0,len(this_level)-1):
                this_level[i].next=this_level[i+1]
        
            if this_level[0].left == None:
                still_working = False
            bfs=this_level
        
        return root
            


Success
Details
Runtime: 64 ms, faster than 58.93% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.7 MB, less than 70.69% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Next challenges:


LEARNED:
	python uses pass by object reference which is niether pass by value nor pass by reference
		mutable because important here
	Breath first search was easiest to do with a while loop
	BFS may be best executed with a while loop

NOTES:
	I wonder how to do bfs recursively and if it is straight forward



