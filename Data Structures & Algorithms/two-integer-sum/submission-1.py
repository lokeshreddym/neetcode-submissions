class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ls_copy = nums.copy()
            diff_number = target-nums[i]
            ls_copy.remove(nums[i])
            if diff_number in ls_copy:
                second_index = ls_copy.index(diff_number)
                second_index = second_index if second_index < i else second_index + 1
                return [i,second_index]
        return []