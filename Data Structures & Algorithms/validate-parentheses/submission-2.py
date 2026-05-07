class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")":"(","]":"[","}":"{"}
        list = []
        if len(s)%2==1 or len(s)==0:
            return False
        

        for i in s:
            if i in dict.values():
                list.append(i)
            else:
                if len(list)>0:
                    if list[-1]!=dict[i]:
                        return False
                    elif list[-1]==dict[i]:
                        list.pop()
                elif len(list)==0:
                    return False
        if len(list)>=1:
            return False
        if len(list)==0:
            return True