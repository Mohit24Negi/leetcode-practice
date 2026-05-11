class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b = ""
        longest = ""
        for i in s:
            while i in b:
                b = b[1:]
            b +=i
            if len(b)> len(longest):
                longest = b
        return len(longest)