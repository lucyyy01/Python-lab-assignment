# Create a program to store the Prices of sold items on a particular day of a shop in a Tuple.
# Perform the following operations:
# a) Print the total number of items sold
# b) Print the price of cheapest item sold
# c) Print the price of costliest item sold
# d) Print the price list in ascending order
# e) Print the number of costliest items sold on the day

# Input prices of items sold
prices = tuple(map(int, input("Enter prices of sold items separated by space: ").split()))

# a) Total number of items sold
print("Total number of items sold:", len(prices))

# b) Cheapest item price
print("Price of cheapest item:", min(prices))

# c) Costliest item price
max_price = max(prices)
print("Price of costliest item:", max_price)

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
count = prices.count(max_price)
print("Number of costliest items sold:", count)