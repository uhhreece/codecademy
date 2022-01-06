weight = 0
price = 0

print('This is a system that is made to calculate shipping prices of your items.')
shipping = input('Please type which type of shipping you want (Ground, Ground Premium, Drone).')
weight = input('How much does the package weigh?')

# ground shipping
if shipping == "Ground":
  if weight <= 2:
    price = weight * 1.5 + 20
  elif weight > 2 and weight <= 6:
    price = weight * 3 + 20
  elif weight > 6 and weight <= 10:
    price = weight * 4 + 20
  elif weight > 10:
    price = weight * 4.75 + 20
print("Ground Shipping $", price)

# ground premium shipping
if shipping == "Ground Premium":
  price = 125
print("Ground Shipping Premium $", price)

# drone shipping
if shipping == "Drone":
  if weight <= 2:
    price = weight * 4.5
  if weight > 2 and weight <= 6:
    price = weight * 9
  if weight > 6 and weight <=10:
    price = weight * 12 
  if weight > 10:
    price = weight * 14.25
print('Drone Shipping Premium $', price)
