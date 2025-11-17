class Solution:
    def numSub(self, s: str) -> int:
        start = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "0":
                start = i+1
            else: result += i-start+1 
        return result%(10**9+7)
        