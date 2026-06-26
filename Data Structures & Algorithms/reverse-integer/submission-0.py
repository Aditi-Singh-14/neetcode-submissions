class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            digit=[int(d) for d in str(abs(x))]
            for i, num in enumerate(digit):
                digit[i]= num*(10**i)
        elif x<0:
            digit=[int(d) for d in str(abs(x))]
            for i, num in enumerate(digit):
                digit[i]= num*(10**i)*-1
        a=sum(digit)
        if a < -2**31 or a > 2**31 - 1:
            return 0
        return a
            