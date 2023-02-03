class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0, 1]
        for i in range(2, n + 1):
            l.append(l[i - 1] + l[i - 2])
        return l[n]
