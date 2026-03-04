# Construct a program to store the following details of a Vendor of a Shop.
# a) Name of vendor
# b) Year of association
# c) Contact number
# d) eMail ID
# Read the details of monthly purchases from Vendor and generate a Annual Purchase/Billing report.

# Vendor Annual Purchase/Billing Report

# Vendor details
name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Monthly purchase details
total = 0
print("\nEnter purchase amount for 12 months:")

for i in range(1, 13):
    purchase = float(input(f"Month {i} purchase: "))
    total += purchase

# Display report
print("\n------ Vendor Annual Purchase Report ------")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase/Billing:", total)