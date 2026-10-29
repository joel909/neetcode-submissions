class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest_difference = 0
        current_smallest = prices[0]
        for price in prices:
            if price<current_smallest:
                current_smallest = price
            else:
                price_difference = price-current_smallest
                if price_difference>largest_difference:
                    largest_difference = price_difference
        return largest_difference

        