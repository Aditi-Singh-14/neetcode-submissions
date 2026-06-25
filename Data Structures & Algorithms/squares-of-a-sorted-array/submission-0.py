class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp=[]
        for i in nums:
            i=i**2
            temp.append(i)
        temp=sorted(temp)
        return temp