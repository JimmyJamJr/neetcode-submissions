class Solution:
    def trap(self, height: List[int]) -> int:
        # water[i] = min(maxLeft[i], maxRight[i]) - height[i]

        maxLeft = [height[0]] * len(height)
        maxRight = [height[-1]] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])

        total = 0
        for i, h in enumerate(height):
            total += max(0, min(maxRight[i], maxLeft[i]) - h)
        return total