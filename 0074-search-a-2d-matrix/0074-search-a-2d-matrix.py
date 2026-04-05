class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0]<=target<=i[-1]:
                if target==i[0] or target==i[-1]:
                    return True
                l,r=0,len(i)-1
                while l<=r:
                    mid=(l+r)//2
                    if target==i[mid]:
                        return True
                    elif target<i[mid]:
                        r=mid-1
                    else:
                        l=mid+1
        return False
            