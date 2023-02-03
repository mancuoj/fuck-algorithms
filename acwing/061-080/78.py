class Solution(object):
    def leftRotateString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if n == 0:
            return s
        n %= len(s)
        return s[n:] + s[:n]
