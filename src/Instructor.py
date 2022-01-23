
from src.DataManager import *


def addHomework(instructorName: str, className: str,
                year: int, homework: str):
    course: Course = findCourse(className, year)
    if not course is None:
        course.addHomework(Homework(homework))


def assignGrade(instructorName: str, className: str,
                year: int, hwName: str, stuName: str, grade: int):
    the_un: Enrollee = findStudent(stuName)
    course: Course = findCourse(className, year)
    if (not the_un is None) and (not course is None):
        homework: Homework = course.getHomework(hwName)
        if not homework is None:
            homework.gradeStudent(the_un, grade)


def homeworkExists(clName: str, year: int, hwName: str) -> bool:
    course: Course = findCourse(clName, year)
    if course is None:
        return False
    return not course.getHomework(hwName) is None


def getGrade(clName: str, year: int, hwName: str, stuName: str) -> int:
    course: Course = findCourse(clName, year)
    the_un: Enrollee = findStudent(stuName)
    if course is None or the_un is None:
        return None
    hw: Homework = course.getHomework(hwName)
    if hw is None:
        return None
    return hw.getGrade(the_un)
