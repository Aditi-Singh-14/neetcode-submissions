class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far=arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            original_val = arr[i]
            arr[i]=max_so_far
            max_so_far = max(max_so_far, original_val)
        return arr