
from course_files.person import Person

person1 = Person('John')
person1.print_info()

person2 = Person('Kate')
# print(person2.get_age())
print(person2.age)
# person2.set_age(25)
person2.age = 35
# print(person2._Person__age)
person2.print_info()
