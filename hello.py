class Employee:
    def __init__(self, name, salary):
        self._name = name           # Protected attribute
        self._salary = salary       # Protected attribute

    @property
    def name(self):
        """Getter for name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name."""
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def salary(self):
        """Getter for salary."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Setter for salary with validation."""
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary must be non-negative")

# Example Usage
emp = Employee("Alice", 50000)

# Accessing and setting values using getter and setter
print(emp.name)       # Getter: Output - Alice
emp.name = "Bob"      # Setter: Changes name to Bob
print(emp.name)       # Output - Bob

print(emp.salary)     # Getter: Output - 50000
emp.salary = 60000    # Setter: Changes salary to 60000
print(emp.salary)     # Output - 60000

# Validation in setter
# emp.salary = -1000  # Raises ValueError: Salary must be non-negative
