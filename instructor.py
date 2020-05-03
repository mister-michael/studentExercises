from nss_person import INSS_Person

class Instructor(INSS_Person):

    def __init__(self, first, last, slack, cohort, specialty):
        INSS_Person.__init__(self)
        self.first = first
        self.last = last
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def assign_ex(self, exercise, *students):
        for student in students:
            student.ex_list.append(exercise)