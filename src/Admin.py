
from src.DataManager import *


def resetAll():
    enrollees = set()
    courseInstructors = dict()


def createClass(className: str, year: int, instructorName: str, capacity: int):
    course: Course = Course(className, year, capacity)
    courseInstructors[course] = instructorName


def changeCapacity(className: str, year: int, capacity: int):
    course: Course = findCourse(className, year)
    if not course is None:
        course.capacity = capacity


def classExists(className: str, year: int) -> bool:
    return findCourse(className, year) != None


def getClassInstructor(className: str, year: int) -> str:
    course: Course = findCourse(className, year)
    if course is None:
        return None
    else:
        return courseInstructors[course]


def getClassCapacity(className: str, year: int):
    course: Course = findCourse(className, year)
    if course is None:
        return -1
    else:
        return course.capacity
