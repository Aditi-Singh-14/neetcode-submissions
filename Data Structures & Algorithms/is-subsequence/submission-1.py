class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers
        i, j = 0, 0
        
        # Traverse both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer for s
            if s[i] == t[j]:
                i += 1
            # Always move the pointer for t
            j += 1
            
        # If we reached the end of s, it is a subsequence
        return i == len(s)
