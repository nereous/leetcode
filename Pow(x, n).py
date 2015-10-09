'''
Implement pow(x, n).
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
        	return 1
        elif n < 0:
        	return 1/self.myPow(x,-n)
        else:
        	goal = self.myPow(x,n/2)
        	if n%2 == 0:
        		return goal*goal
        	else:
        		return goal*goal*x