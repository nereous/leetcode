'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''
class Solution(object):
	'''
  一开始理解错题意了，想成了蓄水池最大蓄水量
	'''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax   = []
        rightmax  = []
        maxheight = 0
        for i in xrange(0,len(height)):
        	if height[i] > maxheight:
        		leftmax.append(height[i])
        		maxheight = height[i]
        	else:
        		leftmax.append(maxheight)
        maxheight = 0
        for x in reversed(height):
        	if x > maxheight:
        		rightmax.append(x)
        		maxheight = x
        	else:
        		rightmax.append(maxheight)

        sum = 0
        for i in xrange(0,len(height)):
        	sum += min(leftmax[i],rightmax[i])
        return sum
'''
挡板，最低挡板与两块挡板距离所容水量
'''
	def maxArea(self, height):
	        """
	        :type height: List[int]
	        :rtype: int
	        """
	        left  = 0
	        right = len(height)-1
	        capability = 0
	        while left <= right:
	        	sum = min(height[left],height[right])*(right-left)
	        	if capability < sum:
	        		capability = sum
	        	if height[left] > height[right]:
	        		right -= 1
	        	else:
	        		left  += 1
	        return capability

        


