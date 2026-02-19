# --- Single Inheritance ---

# Class B inherits from class A.
# This means objects of B can directly use methods defined in A.

class A:
    def show(self):
        print("class A show method")

class B(A):
    # B automatically gets all accessible members of A
    pass

obj = B()
obj.show()   # Calling parent class method using child class object


# --- Single Inheritance using Constructor ---

# Student inherits from Person.
# When a Student object is created, Person's constructor runs automatically.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("name:", self.name)
        print("age:", self.age)

class Student(Person):
    # Student inherits name, age and show_details()
    pass

obj_student = Student("Ak", 22)
obj_student.show_details()   # Accessing parent method


# --- Multiple Inheritance ---
# Bulldog inherits from both Animal and Dog.
# It combines behaviors from both parent classes.

class Animal:
    def show_animal(self):
        print("Animal class")

class Dog:
    def show_dog(self):
        print("Dog class")

class Bulldog(Animal, Dog):
    # Gains methods from both Animal and Dog
    pass

obj1 = Bulldog()
obj1.show_animal()
obj1.show_dog()


# --- Multilevel Inheritance ---
# Inheritance chain: A -> B -> C
# Class C inherits indirectly from A through B.

class A:
    def show_method1(self):
        print("class A")

class B(A):
    def show_method2(self):
        print("class B")

class C(B):
    # C has access to methods of both A and B
    pass

obj = C()
obj.show_method1()
obj.show_method2()


# --- Hierarchical Inheritance ---
# Multiple child classes inherit from the same parent class.

class Person:
    def basic_info(self):
        print("This is common information for all persons")

class Student(Person):
    def student_info(self):
        print("This is student specific information")

class Teacher(Person):
    def teacher_info(self):
        print("This is teacher specific information")

student_obj = Student()
teach_obj = Teacher()

student_obj.basic_info()     # Common method from parent
student_obj.student_info()   # Student-specific method

teach_obj.basic_info()    # Common method from parent
teach_obj.teacher_info()  # Teacher-specific method
