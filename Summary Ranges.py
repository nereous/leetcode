'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result =[]
        if len(nums)<1:
        	return result
        begin  = 0
        string ="%s"%nums[begin]
        listTemp =["%s"%nums[begin]]
        if len(nums)==1:
        	result.append(string)
        	return result
        for j in xrange(1,len(nums)):
        	if nums[j] - nums[begin] == j-begin:
        		if len(listTemp)==1:
        			listTemp.append("%s"%nums[j])
        		else:
        			listTemp[-1] = "%s"%nums[j]
        		continue
        	else:
        		string ='->'.join(listTemp)
        		result.append(string)
        		listTemp =["%s"%nums[j]]
        		begin  = j
        string ='->'.join(listTemp)
        result.append(string)
        return result
a = Solution()
num = [-2147483648,-2147483647,2147483647]
print a.summaryRanges(num)

        	