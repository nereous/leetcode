class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dir ={}
        if len(nums)==0:
            return False
        for i in range(0,len(nums)):
        	if dir.has_key(nums[i])==True:
        		return True
        	else:
        		dir.setdefault(nums[i],0)
        return False

