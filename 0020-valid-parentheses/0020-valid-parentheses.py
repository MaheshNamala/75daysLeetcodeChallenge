class Solution:
    def isValid(self, s: str) -> bool:
        k={"}":"{","]":"[",")":"("}
        v=[]
        for i in s:
            if i in k:
                if v and v[-1]==k[i]:
                    v.pop()
                else:
                    return False
            else:
                v.append(i)
        return not v