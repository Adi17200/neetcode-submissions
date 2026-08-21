class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            lm = rm = height[i]

            for j in range(i):
                lm = max(lm, height[j])
            
            for j in range(i+1, n):
                rm = max(rm, height[j])
            
            res += min(lm, rm)-height[i]

        return res