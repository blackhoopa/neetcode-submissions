class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        max_profit = [0]
        for i, price in enumerate(prices):
            for j in prices[i+1::]:
                net = j - price
                if net <= 0:
                    net = 0
                max_profit.append(net)
        return max(max_profit) 
          
def nth_fibo(n):
    if n==0: return 0
    if n==1: return 1

    F = [None] * (n + 1)
    F[0] = 0
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]