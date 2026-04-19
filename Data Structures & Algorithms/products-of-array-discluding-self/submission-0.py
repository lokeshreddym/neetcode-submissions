class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls= []

        for i in range(len(nums)):
            number = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                number=number*nums[j]
                
            ls.append(number)
        return ls
        