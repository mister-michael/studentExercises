class Instructor:

    def __init__(self, first, last, slack, cohort, specialty):
        self.first = first
        self.last = last
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def assign_ex(self, exercise, *students):
        for student in students:
            student.ex_list.append(exercise)


class Student:

    def __init__(self, first, last, slack, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort = cohort
        self.ex_list = list()

    def add_ex(self, exercise):
        self.ex_list.append(exercise)


class Cohort:

    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)


class Exercise:

    def __init__(self, name, language):
        self.exercise = name
        self.language = language


D38 = Cohort("D38")
D36 = Cohort("D36")

array_methods = Exercise("Array Methods", "javascript")
reactstrap = Exercise("Reactstrap", "javascript")
nutshell_1 = Exercise("nutshell vanilla", "javascript")
make_and_model = Exercise("Make and Model", "python")

mike_prince = Student("Mike", "Prince", "princleySlack", D38)
matty_k = Student("Matt", "K", "theRealnessSlack", D38)
cooper = Student("Cooper", "Nichols", "coopSlack", D36)
cody = Student("Cody", "Murdock", "codyMurdockSlack", D36)

bryan = Instructor("Bryan", "Nilsen", "high555Slack", D36, "high fives")
kristen = Instructor("kristen", "Norris", "kNorrisSlack", D36, "500 m butterfly")
jisie = Instructor("Jisie", "David", "jMoneySlack", D38, "500 m butterfly")

student_list = [mike_prince, matty_k, cooper, cody]
instructor_list = [bryan, kristen, jisie]
cohort_list = [D38, D36]
exercise_list = [array_methods, reactstrap, nutshell_1, make_and_model]

bryan.assign_ex(array_methods.exercise, mike_prince, matty_k, cooper)
bryan.assign_ex(reactstrap.exercise, mike_prince, matty_k, cooper)
bryan.assign_ex(nutshell_1.exercise, mike_prince, matty_k, cooper)
bryan.assign_ex(make_and_model.exercise, cody)


for stud in student_list:
    stud.cohort.add_student(stud)

for inst in instructor_list:
    inst.cohort.add_instructor(inst)


for cohort in cohort_list:
    print(f"------{cohort.name}------")

    for stud in cohort.students:
        i = len(stud.ex_list)
        ex_pen = ""
        for ex in stud.ex_list:
            if len(stud.ex_list) > 1:
                i -= 1
                if i > 0:
                    ex_pen += "".join(ex) + ", "
                elif i == 0:
                    ex_pen += "and " + "".join(ex) + "."
            else:
                ex_pen += f"{ex}" + "."
        print(f"{stud.first_name} {stud.last_name} is working on {ex_pen}")
        print("")
