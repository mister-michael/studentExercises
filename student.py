from nss_person import INSS_Person

class Student(INSS_Person):

    def __init__(self, first, last, slack, cohort):
        INSS_Person.__init__(self)
        self.first = first
        self.last = last
        self.slack = slack
        self.cohort = cohort
        self.ex_list = list()

    def add_ex(self, exercise):
        self.ex_list.append(exercise)