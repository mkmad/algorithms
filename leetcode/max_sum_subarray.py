class Solution(object):
    def __init__(self):
        self.max_sum = 0
        self.max_array = []

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums:
            if len(nums) == 1:
                return nums[0], nums
            mid = len(nums) / 2
            suml, arrayl = self.maxSubArray(nums[:mid])
            sumr, arrayr = self.maxSubArray(nums[mid:])
            sumc, arrayc = self.calculate_crossover(nums, mid)

            if suml > self.max_sum:
                self.max_sum = suml
                self.max_array = arrayl
            elif sumr > self.max_sum:
                self.max_sum = sumr
                self.max_array = arrayr
            elif sumc > self.max_sum:
                self.max_sum = sumc
                self.max_array = arrayc

            if suml > sumr:
                if sumr > sumc:
                    return suml, arrayl
                elif suml > sumc:
                    return suml, arrayl
                else:
                    return sumc, arrayc
            elif sum
            return self.max_sum, self.max_array

        else:
            return 0, []

    def calculate_crossover(self, nums, mid):
        lsum = 0
        rsum = 0
        li = 0
        ri = len(nums) -1
        sum = 0

        if len(nums) == 2:
            return nums[0] + nums[1], nums

        for k in range(mid - 1, 0, -1):
            if nums[k] + lsum > lsum:
                li = k
        for v in range(mid, len(nums) - 1):
            if nums[v] + rsum > rsum:
                ri = v

        for val in range(li, ri):
            sum += nums[val]

        return sum, nums[li:ri + 1]

if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([4,-1,2,1])