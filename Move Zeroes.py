'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        count  = 0
        for i in xrange(0,length):
        	if nums[i]==0:
        		count = count + 1
        nums[:]=[x for x in nums[0:length] if x!=0]
        nums.extend([0]*count)




if __name__ == "__main__":
	a = Solution()
	num = [0,1,0,3,12]     
	a.moveZeroes(num)
	print num	
