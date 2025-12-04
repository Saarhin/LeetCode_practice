class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1

        while start <= end:
            middle = (start+end)//2

            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                start = middle + 1
            else:
                end = middle - 1
        return start