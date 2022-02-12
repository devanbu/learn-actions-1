from typing import Optional
from src.DataManager import Course, Homework, Enrollee, findCourse,findStudent


def addHomework(className: str,
                year: int, homework: str) -> None:
    course: Optional[Course] = findCourse(className, year)
    if not course is None:
        course.addHomework(Homework(homework))


def assignGrade(className: str,
                year: int, hwName: str, stuName: str, grade: int) -> None:
    the_un: Enrollee = findStudent(stuName)
    course: Optional[Course] = findCourse(className, year)
    if (not the_un is None) and (not course is None):
        homework: Optional[Homework] = course.getHomework(hwName)
        if not homework is None:
            homework.gradeStudent(the_un, grade)


def homeworkExists(clName: str, year: int, hwName: str) -> bool:
    course: Optional[Course] = findCourse(clName, year)
    if course is None:
        return False
    return not course.getHomework(hwName) is None


def getGrade(clName: str, year: int, hwName: str, stuName: str) -> Optional[int]:
    course: Optional[Course] = findCourse(clName, year)
    the_un: Enrollee = findStudent(stuName)
    if course is None or the_un is None:
        return None
    hw: Optional[Homework] = course.getHomework(hwName)
    if hw is None:
        return None
    return hw.getGrade(the_un)
