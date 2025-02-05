weight = 41.5
weightds = 41.5
#Ground Shipping
#p3 = price per pound
premium_ground_cost = 125
print("Premium ground cost is 125£, do not forget pls!")
if weight <= 2:
  p3 = 1.50
elif weight <= 6:
  p3 = 3
elif weight <= 10:
  p3 = 4
elif weight > 10:
  p3 = 4.75
else:
  p3 = 0
if p3 > 0:
  cost1 = weight * p3 + 20
print(cost1)
#Drone Shipping
if weightds <= 2:
  p3 = 4.50
elif weightds <= 6:
  p3 = 9
elif weightds <= 10:
  p3 = 12
elif weightds > 10:
  p3 = 14.25
else:
  p3 = 0
if p3 > 0:
  cost2 = weightds * p3
print(cost2)
if cost1 > cost2:
  print("Drone shipping is cheaper!")
elif cost1 < cost2:
  print("Ground shipping is cheaper!")
else:
  print("Choose a product you want to buy first")
if cost1 > premium_ground_cost and cost2 > premium_ground_cost:
  print("Premium Ground shipping will cost you only 125£ since total price is above 125£ by both delivery methods!")
else:
  print("")
