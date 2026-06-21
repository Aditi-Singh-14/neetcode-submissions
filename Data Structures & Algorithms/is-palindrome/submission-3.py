class Solution(object):
    def isPalindrome(self, s):
        c=[]
        for st in s:
            if st.isalnum()==True:
                c+=st
        a="".join(c)
        if a.lower()==a[::-1].lower():
            return True    
        return False