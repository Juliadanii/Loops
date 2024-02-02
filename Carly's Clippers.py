hairstyle = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

costs = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_cost = 0
for cost in costs:
  total_cost += cost
average_cost = total_cost / len(costs)
print(f"Average Haircut Price: {average_cost}")
new_prices = [elem - 5 for elem in costs]
print(new_prices)
total_revenue = 0
for i in range(len(hairstyle)):
  total_revenue += costs[i] * last_week[i]
print(f"Total Revenue: {total_revenue}")
average_daily_revenue = total_revenue / 7
print(f"average_daily_revenue: {average_daily_revenue}")
cuts_under_30 = [hairstyle[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
