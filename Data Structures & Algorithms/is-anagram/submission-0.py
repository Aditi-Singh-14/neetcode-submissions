class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=dict(Counter(s))
        t=dict(Counter(t))
        if s==t:
            return True
        else:
            return False