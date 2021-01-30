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
        print ("I'm normal worker. I'm working.")

    def eat(self):
        print ("Lunch break....(5 secs)")
        time.sleep(5)

class SuperStudent(AbstractStudent):

    def study(self):
        print ("I'm super worker. I work very hard!")

    def eat(self):
        print ("Lunch break....(3 secs)")
        time.sleep(3)


class School(object):

    def __init__(self):
        self.student = None

    def set_student(self, student):
        assert isinstance(student, AbstractStudent), "`worker` must be of type {}".format(AbstractStudent)

        self.student = student

    def manage(self):
        self.student.work()

    def lunch_break(self):
        self.student.eat()


class Robot(AbstractStudent):

    def study(self):
        print ("I'm a robot. I'm working....")

    def eat(self):
        print ("I don't need to eat....")   # This code doing nothing but it is a must. (Bad!)

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