'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        if len(citations)==0:
            return 0
        citations.sort(reverse = True)
        for i ,item in enumerate(citations):
        	if i+1<=item:
        		result = i+1
        	else:
        		break 
        return result
'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        left   = 0
        if len(citations)==0:
        	return 0
        right = len(citations) - 1
        while left<=right:
        	mid = left + (right-left)/2
        	if citations[mid]>len(citations)-mid:
        		right  = mid - 1
        	elif citations[mid]==len(citations)-mid:
        		return len(citations) - mid
        	else:
        		left   = mid + 1
        return len(citations) - left
 
