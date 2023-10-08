# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        """
        i=j=k=0
        merged=[0]*(m+n)

        while i<m and j<n:
            if nums1[i] < nums2[j]:
                merged[k]=nums1[i]
                i+=1
            else:
                merged[k]=nums2[j]
                j+=1
            k+=1

        while i<m :
            merged[k]=nums1[i]
            i+=1
            k+=1

        while j<n:

            merged[k]=nums2[j]
            j+=1
            k+=1
            
        for i in range(m+n):

            nums1[i]=merged[i]


# Runtime: 10 ms, faster than 98.49% of Python online submissions for Merge Sorted Array.
# Memory Usage: 13.4 MB, less than 19.77% of Python online submissions for Merge Sorted Array.