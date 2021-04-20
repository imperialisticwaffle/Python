# We can define our own variables essentially using classes.
class college_student: # The text coming after "class" is the name of our class.
    # This is an "initialize" function, the first necessary step. __init__ and (self) go together.
    # Variables after "self" are attributes of the class. is_on_probation will be a boolean value.
    def __init__(self, name, major, gpa, is_on_probation): 
        self.name = name 
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# We have now defined a class and can create a "student", or object, by giving it information.
    # Class college_student can now be imported to other files.
college_student_1 = college_student("Jim", "Business", 4.0, False)
# We can access each entry/attribute.
print(college_student_1.name)
print(college_student_1.major)

# We can define a second object.
college_student_2 = college_student("Pam", "Biology", 2.8, True)
print(college_student_2.name)
