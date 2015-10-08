'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dir = {}
        longsest = 0
        for x in nums:
        	if dir.has_key(x) == False:
        		dir.setdefault(x,0)
        for x in nums:
        	if dir[x] == 1:
        		continue
        	length = 1
        	data = x + 1
        	while dir.has_key(data) == True:
        		dir[data] =1
        		data += 1
        		length += 1
        	data = x - 1 
        	while dir.has_key(data) == True:
        		dir[data] =1
        		data -= 1
        		length += 1
        	longest = max(longest,length)
        return longest



