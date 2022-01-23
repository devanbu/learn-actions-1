
from src.DataManager import *


def registerForClass(stuName: str, clName: str, year: int):
    the_un: Enrollee = findStudent(stuName)
    course: Course = findCourse(clName, year)
    if not (course is None or the_un is None):
        the_un.addCourse(course)
        course.addStudent(the_un)
        return
    return


def dropClass(stuName: str, clName: str, year: int):
    the_un: Enrollee = findStudent(stuName)
    course: Course = findCourse(clName, year)
    if not (course is None or the_un is None):
        the_un.addCourse(course)
        course.removeStudent(the_un)
    return


def submitHomework(stuName: str, hwName: str, answer: str,
                   clName: str, year: int):
    the_un: Enrollee = findStudent(stuName)
    course: Course = findCourse(clName, year)
    if not (course is None or the_un is None):
        hw: Homework = course.getHomework(hwName)
        if not hw is None:
            hw.submit(the_un, answer)


def isRegisteredFor(stuName: str, clName: str, year: int) -> bool:
    the_un: Enrollee = findStudent(stuName)
    course: Course = findCourse(clName, year)
    if not (course is None or the_un is None):
        return the_un in course.getEnrollees()
    return False


def hasSubmitted(stuName: str, hwName: str, clName: str, year: int) -> bool:
    the_un: Enrollee = findStudent(stuName)
    course: Course = findCourse(clName, year)
    if not (course is None or the_un is None):
        hw: Homework = course.getHomework(hwName)
        if not hw is None:
            return not hw.getSubmission(the_un) is None
    return False
