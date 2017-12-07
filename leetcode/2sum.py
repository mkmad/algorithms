class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        elif not target:
            return []
            
        dict_ = {}
        import ipdb; ipdb.set_trace()
        for val in range(len(nums)):
            if nums[val] in dict_:
                return [dict_[(target - nums[val])], val]
            else:
                dict_[(target - nums[val])] = val

if __name__ == '__main__':
    s = Solution()
    s.twoSum([2, 7, 11, 15], 9)
