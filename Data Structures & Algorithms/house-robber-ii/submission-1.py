class Solution:
    def solve(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, n):
            pick = nums[i] + prev2
            not_pick = prev1
            curr = max(pick, not_pick)
            
            prev2 = prev1
            prev1 = curr
        
        return prev1

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        x = self.solve(nums[0:n-1])   # exclude last house
        y = self.solve(nums[1:n])     # exclude first house
        return max(x, y)