'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        data_plus = 1
        temp =[1]
        for i in range(0,len(digits))[::-1]:#逆序遍历的方式，[::-1]
        	sum = digits[i]+data_plus
        	if sum<10:
        		digits[i] = sum
        		data_plus =0
        		break
        	else:
        		digits[i] = sum % 10
        if data_plus == 1:
            temp.extend(digits)
            return temp
        else:
            return digits
 

        		