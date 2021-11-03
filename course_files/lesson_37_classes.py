
from course_files.person import Person, Employee

person = Person('John', 30)
person.age = 35
person.print_info()

employee = Employee('Nick', 30)
employee.print_info()
employee.more_info()
