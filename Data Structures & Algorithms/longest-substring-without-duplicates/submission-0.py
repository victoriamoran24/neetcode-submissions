class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = set([])
        ans = 0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans
