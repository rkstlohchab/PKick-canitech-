class Base():
    def __init__(self, physics, chemistry, maths):
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def check_marks(self):
        marks_list = [{mark1: "self.physics", mark2: "self.chemistry", mark3: "self.maths"}]
        for i in marks_list:
            if i > 100 or i < 0:
                raise

    def marks_maths(self):
        self.check_marks()
        print(self.maths)

    def marks_physics(self):
        self.check_marks()
        print(self.physics)

    def marks_chemistry(self):
        self.check_marks()
        print(self.chemistry)

class StdMarks():
    

number = StdMarks(physics=87,chemistry=77, maths=11)
number.marks_maths()
number.marks_physics()
number.marks_chemistry()