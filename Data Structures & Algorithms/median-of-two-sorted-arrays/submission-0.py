class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        merge = nums1 + nums2

        merge.sort()

        totallen = len(merge)

        if totallen % 2 == 0:
            return (merge[totallen // 2 -1]+ merge[totallen // 2]) / 2.0

        else:
            return merge[totallen // 2]