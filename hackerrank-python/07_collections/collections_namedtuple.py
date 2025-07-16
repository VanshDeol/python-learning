from collections import namedtuple

number_of_students = int(input())
Student = namedtuple('Student', input().split())
marks = 0
for i in range(number_of_students):
    student = Student(*input().split())
    marks += int(student.MARKS)
print(f"{marks/number_of_students:.2f}")



'''

------shorter version using generator expression------

from collections import namedtuple
number_of_students = int(input())
Student = namedtuple('Student', input().split())
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(number_of_students)) / number_of_students:.2f}")
'''

