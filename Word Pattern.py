'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) == 0 and len(str) == 0:  
            return True  
        elif len(pattern) == 0 or len(str) == 0:  
            return False

        mymap    = {}
        mystring = {}
        list_str = str.split(" ")
        if len(pattern)!=len(list_str):
        	return False
        for i,item in enumerate(list_str):
        	if mymap.has_key(pattern[i]) == False:
        		if mystring.has_key(list_str[i]) == False:
        			mymap[pattern[i]] = list_str[i]
        			mystring[list_str[i]] = pattern[i]
        		else:
        			return False
        	else:
        		if mymap[pattern[i]] == list_str[i]:
        			continue
        		else:
        			return False
        return True


