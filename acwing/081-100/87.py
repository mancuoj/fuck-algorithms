class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        if s == "":
            return 0

        i, sign, ans = 0, 1, 0
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                sign = -1
            i += 1

        while i < len(s) and "0" <= s[i] <= "9":
            ans = ans * 10 + (ord(s[i]) - 48)
            i += 1

        ans *= sign
        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648
        return ans
