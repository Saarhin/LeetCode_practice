class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_val_added = nums[0]
        last_index_added = 0

        for i in nums:
            if i != last_val_added:
                last_val_added = i
                last_index_added +=1
                nums[last_index_added] = i

        return last_index_added+1