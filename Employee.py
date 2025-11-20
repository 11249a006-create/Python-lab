class Employee:
    def __init__(self, name, emp_id, dept, salary):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self.salary = salary

    def update_salary(self, dept, new_salary):
        if self.dept == dept:
            self.salary = new_salary


emp = Employee("Rahul", 101, "IT", 50000)
emp.update_salary("IT", 60000)
print(emp.name, emp.emp_id, emp.dept, emp.salary)
