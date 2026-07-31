class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # minimum is somewhere to the right of mid
                left = mid + 1
            else:
                # nums[mid] <= nums[right] means mid could be the min,
                # so keep it in range
                right = mid
        return nums[left]