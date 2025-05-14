def stock_picker(prices)
  best_buy = 0
  best_sell = 0
  max_profit = 0

  left = 0 
  right = 1

  while right < prices.length
    current_profit = prices[right] - prices[left]
    if current_profit > max_profit
      max_profit = current_profit
      best_buy = left
      best_sell = right 
    else
      left = right
    end
    right += 1
  end
  return [best_buy, best_sell]
end



p stock_picker([17,3,6,9,15,8,6,1,10])