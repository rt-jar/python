class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        result = ""
        for l in s:
            if l.isalpha():
                result += l
            else:
                temp = result
                for i in range(int(l) -1):
                    temp += result
                    if len(result) >= k:
                        break
                result = temp
            if len(result) >= k:
                return result[k-1]


s = Solution()
print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 10))