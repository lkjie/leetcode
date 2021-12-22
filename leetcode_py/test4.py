from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1r, n2r = len(nums1), len(nums2)
        pl, ph = 0, n1r
        k = (n1r + n2r + 1) // 2
        while pl < ph:
            pmid1 = (pl + ph) // 2
            pmid2 = k - pmid1
            if nums1[pmid1] < nums2[pmid2-1]:
                pl = pmid1 + 1
            else:
                ph = pmid1
        pmid1 = pl
        pmid2 = k - pmid1
        maxleft = max(nums1[pmid1-1] if pmid1 > 0 else -1e10, nums2[pmid2-1] if pmid2 > 0 else -1e10)
        minright = min(nums1[pmid1] if pmid1 < n1r else 1e10, nums2[pmid2] if pmid2 < n2r else 1e10)
        if (n1r + n2r) % 2 == 0:
            return (maxleft + minright) / 2.0
        else:
            return maxleft


if __name__ == '__main__':
    s = Solution()
    p = (
        [1, 3, 5, 8, 9, 11],
        [2, 4, 7, 10, 12, 13]
    )
    p = (
        [1,],
        []
    )
    r = s.findMedianSortedArrays(*p)
    print(r)