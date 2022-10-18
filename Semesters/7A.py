
class Student:
    def _init_(self, name, sex, course, results):
        self.name = name
        self.sex = sex
        self.course = course
        self.results = results
    def display(self, name, sex, course, results):
        self.name = name
        self.sex = sex
        self.course = course
        self.results = results
        print("Name : ", self.name)
        print("Sex : ", self.sex)
        print("Course : ", self.course)
        print("Results : ", self.results)

s1 = Student()
s1.display('Reuben', 'M', 'BSc IT', '96.8%')

