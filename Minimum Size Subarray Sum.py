'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        mindistance = len(nums)+1
        first = 0
        last  = 0
        Mysum   = 0
      	while first <= last and Mysum < s and last < len(nums):
      		Mysum += nums[last]
      		while first <= last and Mysum >= s:
      			mindistance = min(mindistance,last-first+1)
      			Mysum -= nums[first]
      			first += 1
      		last += 1
      	if mindistance == len(nums)+1:
      		return 0
      	else:
      		return mindistance


      		


