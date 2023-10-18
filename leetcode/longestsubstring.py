class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subStr = {}

        for i in range(len(s)):
            tempStr = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in tempStr:
                    tempStr += s[j]
                else:
                    break
            subStr[len(tempStr)]=tempStr

         
        print(subStr)
        return list(subStr.keys())[-1]


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))