class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count=text.count('b')
        a_count=text.count('a')
        l_count=text.count('l')
        o_count=text.count('o')
        n_count=text.count('n')
        l_count=l_count//2
        o_count = o_count // 2
        return min(b_count, a_count, l_count, o_count, n_count)