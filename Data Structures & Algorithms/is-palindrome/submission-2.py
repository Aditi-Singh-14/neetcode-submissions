class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=str()
        for st in s:
            if st.isalnum()==True:
                c+=st
        if c.lower()==c[::-1].lower():
            return True
        return False