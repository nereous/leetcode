'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        idx_top    = 0
        idx_bottom = len(matrix)-1
        idx_left   = 0
        idx_right  = len(matrix[0])-1
        search_data= matrix[0][idx_right]
        while idx_left <= idx_right and idx_top <= idx_bottom:
        	search_data= matrix[idx_top][idx_right]
        	if search_data < target:
        		idx_top += 1
        	elif search_data > target:
        		idx_right -= 1
        	else:
        		return True
        return False


