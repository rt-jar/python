class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        binarySize = max(len(a), len(b))
        #make both string of same length
        a = format(a, f"0>{binarySize}")
        b = format(b, f"0>{binarySize}")
        result = [0]*binarySize
        carry = 0
        for i in range(binarySize-1, -1, -1):
            result[i] = int(a[i]) + int(b[i]) + carry
            carry = result[i]//2
            result[i] = str(result[i]%2)

        if carry == 1:
            return ''.join(["1"] + result)
        
        return ''.join(result)

s = Solution()
print(s.addBinary("101", "101"))