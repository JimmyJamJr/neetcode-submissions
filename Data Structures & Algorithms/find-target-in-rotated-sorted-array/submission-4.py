class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # left half sorted
            if nums[l] <= nums[mid]:
                # target in left half for sure
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right half sorted
            else:
                # target in right half for sure
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
            