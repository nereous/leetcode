'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum   = 1
        count = 0
        result = []
        for data in nums:
        	if data != 0 :
        		sum = sum * data
        	else:
        		count += 1
        if count > 1:
        	result = [0]*len(nums)
        	return result
        elif count ==1:
        	for x in nums:
        		if x == 0:
        			result.append(sum)
        		else:
        			result.append(0)
        else:
        	result =[sum/x for x in nums]
        return result
