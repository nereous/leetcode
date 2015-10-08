'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result =[]
        if len(nums)<=1:
        	return nums
        numfirst  = nums[0]
        numsecond = nums[0]
        fircount  = 0
        seccount  = 0
        for x in xrange(0,len(nums)):
        	if nums[x] == numfirst or fircount == 0:
        		numfirst = nums[x]
        		fircount += 1
        	elif nums[x] == numsecond or seccount == 0:
        		numsecond = nums[x]
        		seccount += 1
        	else:
        		fircount -= 1
        		seccount -= 1
        fircount  = 0
        seccount  = 0
        for i in xrange(0,len(nums)):
        	if nums[i] == numfirst:
        		fircount += 1
        	elif nums[i] == numsecond:
        		seccount += 1
        	else:
        		pass
        if fircount > len(nums)/3.:
            result.append(numfirst)
        if numfirst != numsecond and seccount > len(nums)/3.:
            result.append(numsecond)
        else:
        	pass
        return result


        	