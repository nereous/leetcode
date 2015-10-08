'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dir = {}
        for i in xrange(0,len(nums)):
        	if dir.has_key(nums[i])!=True:
        		dir.setdefault(nums[i],i)
        	else:
        		if i-dir[nums[i]]<=k:
        			return True
        		else:
        			dir[nums[i]] =i
        return False