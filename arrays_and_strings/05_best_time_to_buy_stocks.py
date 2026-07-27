class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minimum_price = prices[0]
        maximum_profit = 0

        for price in prices[1:]:
            profit = price - minimum_price
            if profit > maximum_profit:
                maximum_profit = profit

            if price < minimum_price:
                minimum_price = price   

        return maximum_profit

    def display_result(self,prices):
        print(self.maxProfit(prices))


S1 = Solution()

S1.display_result([10,20,83,43,40,22,90,82])