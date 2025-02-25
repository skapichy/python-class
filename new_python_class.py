class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade    
## we are creating a class cousre, so we can add a student to a class
class Course:
    def __init__(self, name, max_students): 
        self.name = name
        self.max_students = max_students
        self.students = [] ## Add method that will allow us add students to this course

## Create a student object inorder to add object to the list  
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True  
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            
        return value/len(self.students)    
    
s1 = Student("Micheal", 24, 89)
s2 = Student("Michelle", 32, 96)
s3 = Student("Timothy", 27, 79)
s4 = Student("Bill", 28, 91)   

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.students[1].name)
print(course.get_average_grade())


## INHERITANCE
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"My name is {self.name}, and I am {self.age} years old.") 
    
class Cat(Pet):
    def speak(self):
        print("Meow")
class Dog(Pet):
    def speak(self):
        print("Woof")
 
cat = Cat("Whiskers", 5)  
cat.show()                            
p = Pet('Bingo', 3)
p.show()
