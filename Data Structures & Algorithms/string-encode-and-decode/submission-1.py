class Solution:

    def encode(self, strs: List[str]) -> str:
        final_list=[]
        for i in strs:
            length=len(i)
            string=str(length)+'#'+i
            final_list.append(string)
        final_string=''.join(i for i in final_list)
        return final_string
    def decode(self, s: str) -> List[str]:
        output_list=[]
        while s:
            hash_index = s.find('#')
            length = int(s[:hash_index])   # get full length
            word = s[hash_index+1 : hash_index+1+length]
            output_list.append(word)
            s = s[hash_index+1+length:]
        return output_list
