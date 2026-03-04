#Construct a program to store the information of an employee such as name, employee ID, department and generate
# the salary as per the following conditions:
# (i) DA is 92% of Basic Salary
# (ii) HRA is 58% of Basic Salary
# (iii) TA is 30% of Basic Salary
# (iv) LIC is deducted: Rs. 500 every month.

# Employee Salary Calculation Program

# Input employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculations
DA = 0.92 * basic_salary
HRA = 0.58 * basic_salary
TA = 0.30 * basic_salary
LIC = 500

gross_salary = basic_salary + DA + HRA + TA
net_salary = gross_salary - LIC

# Display details
print("\nEmployee Details")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)

print("\nSalary Details")
print("Basic Salary:", basic_salary)
print("DA:", DA)
print("HRA:", HRA)
print("TA:", TA)
print("Gross Salary:", gross_salary)
print("LIC Deduction:", LIC)
print("Net Salary:", net_salary)