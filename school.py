from abc import ABCMeta, abstractmethod
import time

class AbstractStudent(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Student(AbstractStudent):

    def study(self):
        print ("Aku pelajar. aku lagi belajar ")

    def eat(self):
        print ("Lunch time....(5 secs)")
        time.sleep(5)

class SuperStudent(AbstractStudent):

    def study(self):
        print ("Aku pelajar yang giat. ak giat belajar !")

    def eat(self):
        print ("Lunch break....(3 secs)")
        time.sleep(3)

class School(object):

    def __init__(self):
        self.student = None

    def set_student(self, student):
        assert isinstance(student, AbstractStudent), "`student` must be of type {}".format(AbstractStudent)

        self.student = student

    def manage(self):
        self.student.study()

    def lunch_break(self):
        self.student.eat()


class Robot(AbstractStudent):

    def study(self):
        print ("Aku robot. aku lagi belajar...")
    def eat(self):
        print("Aku tidak makan")

def main():

    school = School()
    school.set_student(Student())

    school.manage()

    school.lunch_break()

    school.set_student(SuperStudent())
    school.manage()
    school.lunch_break()

    school.set_student(Robot())
    school.manage()
    school.lunch_break()

if __name__ == '__main__':
    main()