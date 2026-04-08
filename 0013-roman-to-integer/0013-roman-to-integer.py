class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }
        total = 0
        for i in range(1,len(s)):
            if value[s[i-1]] < value[s[i]]:
                total -= value[s[i-1]]
            else:
                total += value[s[i-1]]
        total += value[s[-1]]
        return total