class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=[]
        for i in range(len(numbers)):
            target_check = target-numbers[i]
            for j in range(i+1,len(numbers)):
                if target_check==numbers[j]:
                    seen.append([i+1,j+1])
        return seen[0]
                
        