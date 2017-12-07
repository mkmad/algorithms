class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if not nums1:
            return self.calculate_median('right', nums2)[1]
        if not nums2:
            return self.calculate_median('left', nums1)[1]

        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2.00

        resl = self.calculate_median('left', nums1)
        resr = self.calculate_median('right', nums2)
        lm, left = resl[0], resl[1]
        rm, right = resr[0], resr[1]

        if lm == rm:
            return lm
        else:
            if len(nums1) == 1:
                left = 0
            if len(nums2) == 1:
                right = 1
            return self.findMedianSortedArrays(nums1[left:], nums2[:right])

    def calculate_median(self, type, nums):
        if len(nums) == 1:
            return (0,nums[0])
        if type == 'left':
            if len(nums) % 2 != 0:
                lm = nums[len(nums) / 2]
                left = (len(nums) / 2) + 1
            else:
                lm = (nums[(len(nums) / 2) - 1] + nums[(len(nums) / 2)]) / 2.00
                left = len(nums) / 2
            return (lm, left)
        else:
            if len(nums) % 2 != 0:
                rm = nums[len(nums) / 2]
                right = (len(nums) / 2) + 1
            else:
                rm = (nums[(len(nums) / 2) - 1] + nums[(len(nums) / 2)]) / 2.00
                right = len(nums) / 2
            return (rm, right)


if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1, 3], [2])