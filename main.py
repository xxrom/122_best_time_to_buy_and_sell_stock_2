from typing import List


class Solution:

  def maxProfit(self, prices: List[int]) -> int:
    minItem = prices[0] if len(prices) > 0 else None
    fullSum = 0

    for value in prices:
      # print('step: value = %d, minItem = %d, currentSum = %d ' %
      #       (value, minItem, currentSum))

      if value < minItem:
        minItem = value

      if value - minItem > 0:
        fullSum += value - minItem
        minItem = value

    return fullSum
