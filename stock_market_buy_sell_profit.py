def max_prof(price,start,end):
  if (end <= start):
    return 0
  profit = 0
  for i in range(start,end):
    for j in range(i+1, end+1):
      if (price[j] > price[i]):
        curr_profit = price[j] - price[i]
        profit = max(profit, curr_profit)
  return profit
if __name__ == "__main__":
  n = len(price)
  print(max_prof(price,0,n-1))
