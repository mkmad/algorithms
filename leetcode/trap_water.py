class Solution(object):
    def trap(self, height):
        stack = list()
        index = 0
        water = 0
        while index < len(height):
            if len(stack) == 0 or height[index] <= height[stack[len(stack) - 1]]:
                stack.append(index)
                index += 1
            else:
                bottom = stack.pop()
                if len(stack) != 0:
                    water += (min(height[stack[len(stack) - 1]], height[index]) - height[bottom]) * (
                    index - stack[len(stack) - 1] - 1)
        return water

if __name__ == '__main__':
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])