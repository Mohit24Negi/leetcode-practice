class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = 1
        i = 0
        num=""

        if s[i]== '-':
            sign = -1
            i +=1
        elif s[i] == "+":
            sign = +1
            i +=1

        while i < len(s) and s[i].isdigit():
            num += s[i]
            i +=1

        if num== "":
            return 0
        result = sign * int(num)

        if result < -2**31:
            result = -2**31
        if result > 2**31 -1:
            result = 2**31 -1
        return result