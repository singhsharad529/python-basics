# Types of methods
# 1.Instance
# 2.Class
# 3. Static : Not belongs to class and instance as well

# Getter==accessor in Python
# Setter==mutators in python

class Student:
    school = "sharad"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # accessors
    def get_m1(self):
        return self.m1

    # mutators
    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is student class.. and abc module")


s1 = Student(34, 67, 32)
s2 = Student(86, 32, 12)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
