class Solution:
    def climbStairs(self, n: int) -> int:
        #Can also write Fibonacci series for this
        # if n <= 2:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        u = 1
        v = 0
        sum = u+v
        for i in range(n):
            sum = u+v
            temp = u
            u = sum
            v = temp  
        return sum