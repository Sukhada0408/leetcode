class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            sub = []
            for j in range(i,len(s)):
                if s[j] not in sub:
                    sub.append(s[j])
                else:
                    longest = max(longest, len(sub))
                    sub = []
                    break
            longest = max(longest, len(sub))
            if j == len(s)-1:
                break
        return longest