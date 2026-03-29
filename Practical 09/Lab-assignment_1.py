# Practical 09, Lab Assignment 1
# Employee and Manager classes for 10 managers.

class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")


class Manager(Employee):
    def __init__(self, name, age, salary, address, department):
        super().__init__(name, age, salary, address)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")
        print('-' * 40)


def get_manager_input(index):
    print(f"Enter details for manager {index}:")
    name = input('Name: ').strip()
    age = input('Age: ').strip()
    salary = input('Salary: ').strip()
    address = input('Address: ').strip()
    department = input('Department: ').strip()
    return Manager(name, age, salary, address, department)


def main():
    managers = []
    count = 10
    for i in range(1, count + 1):
        managers.append(get_manager_input(i))
        print()

    print('\nDetails of all managers:')
    for manager in managers:
        manager.display()


if __name__ == '__main__':
    main()
