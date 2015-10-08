'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

'''
class Solution(object):
    def findMedian(self,nums1,lenN,nums2,lenM,idx):
        if lenN < lenM :
            return self.findMedian(nums2,lenM,nums1,lenN,idx)
        if lenM == 0:
            return nums1[idx-1]
        if idx == 1:
            return min(nums1[0],nums2[0])
        else:
            first  = min(idx/2,lenM)
            second = idx - first
            if nums2[first-1] < nums1[second-1]:
                temp = nums2[first:]
                return self.findMedian(nums1,lenN,temp,len(temp),idx-first)
            elif nums2[first-1] > nums1[second-1]:
                temp = nums1[second:]
                return self.findMedian(temp,len(temp),nums2,lenM,idx-second)
            else:
                return nums2[first-1]
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1)+len(nums2)
        if total % 2 == 1:
            return self.findMedian(nums1,len(nums1),nums2,len(nums2),total/2 + 1)
        else:
            return (self.findMedian(nums1,len(nums1),nums2,len(nums2),total/2 + 1)+ self.findMedian(nums1,len(nums1),nums2,len(nums2),total/2 ))/2.
    
