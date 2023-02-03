class Solution(object):
    def getSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        return (n * (n + 1)) // 2
