class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        visited = []
        temp_list = []
        for i in range(0,len(strs)):
            for j in range(i,len(strs)):
                if sorted(strs[i])==sorted(strs[j]) and j not in visited:
                    temp_list.append(strs[j])
                    visited.append(j)            
            if len(temp_list)>0:
                output.append(temp_list)
                temp_list=[]
        return output

                    
