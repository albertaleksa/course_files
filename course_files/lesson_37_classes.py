
from course_files.person import Person, Employee

person = Person('John', 30)
person.age = 35
person.print_info()

print(person)

employee = Employee('Nick', 30, 'Google')
employee.print_info()
employee.more_info()

print(employee)
