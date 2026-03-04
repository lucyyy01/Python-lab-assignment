# a) Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the
# current (I) using Ohm’s Law.
# b) Modify the above program to display the nature of current:
# If current &lt; 0.5 A, print “Low current”
# If 0.5 A ≤ current ≤ 2 A, print “Normal current”
# If current &gt; 2 A, print “High current

# Ohm's Law: I = V / R

# Input voltage and resistance
V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R): "))

# Calculate current
I = V / R

print("Current (I) =", I, "Ampere")

# Check nature of current
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")