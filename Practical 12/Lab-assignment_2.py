# Practical 12, Lab Assignment 2
# Read employee.xlsx and print requested reports.

import os

try:
    import pandas as pd
except ImportError:
    print('Pandas is required for this script. Install it with pip install pandas.')
    raise


SAMPLE_EMPLOYEES = [
    {'Employee ID': 'E001', 'Employee Name': 'Amit Kumar', 'Department': 'Automotive', 'Designation': 'Developer'},
    {'Employee ID': 'E002', 'Employee Name': 'Neha Singh', 'Department': 'Banking', 'Designation': 'Tester'},
    {'Employee ID': 'E003', 'Employee Name': 'Rohit Sharma', 'Department': 'Automotive', 'Designation': 'Developer'},
    {'Employee ID': 'E004', 'Employee Name': 'Priya Shah', 'Department': 'Retail', 'Designation': 'Manager'},
    {'Employee ID': 'E005', 'Employee Name': 'Suresh Patel', 'Department': 'Automotive', 'Designation': 'Support Engineer'},
]


def load_employees(file_path):
    if file_path and os.path.isfile(file_path):
        return pd.read_excel(file_path)

    csv_path = os.path.join(os.path.dirname(__file__), 'employee.csv')
    if os.path.isfile(csv_path):
        return pd.read_csv(csv_path)

    return pd.DataFrame(SAMPLE_EMPLOYEES)


def main():
    file_path = input('Enter the path to employee.xlsx (leave blank to use sample data): ').strip()
    df = load_employees(file_path)

    print('\nEmployees working in Automotive domain:')
    auto_employees = df[df['Department'].str.contains('Automotive', case=False, na=False)]
    print(auto_employees.to_string(index=False) if not auto_employees.empty else 'No employees found in Automotive domain.')

    employee_id = input('\nEnter the Employee ID to look up: ').strip()
    if employee_id:
        employee_search = df[df['Employee ID'].astype(str).str.strip().eq(employee_id)]
        if not employee_search.empty:
            print('\nEmployee details:')
            print(employee_search.to_string(index=False))
        else:
            print('Employee ID not found.')

    print('\nList of all Developers:')
    developers = df[df['Designation'].str.contains('Developer', case=False, na=False)]
    print(developers.to_string(index=False) if not developers.empty else 'No developers found.')


if __name__ == '__main__':
    main()
