'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def getnodenum(self,node):
		if node == None:
			return 0
		else:
			return 1 + self.getnodenum(node.left) + self.getnodenum(node.right)
    def kthSmallest(self, root, k):
        if root == None:
            return 0
        leftnum = self.getnodenum(root.left)
        if k == leftnum + 1:
        	return root.val
        elif k < leftnum + 1:
        	return self.kthSmallest(root.left,k)
        else:
        	return self.kthSmallest(root.right,k-leftnum-1)