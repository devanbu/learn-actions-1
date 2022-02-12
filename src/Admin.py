from typing import Optional

from src.DataManager import Course
from src.DataManager import courseInstructors
from src.DataManager import findCourse



def createClass(className: str, year: int, instructorName: str, capacity: int):
    """Creates a new class

    Args:
        className (str): Name of the class/course
        year (int): year Calendar year in which the course is to be taught
        instructorName (str): instructorName Name of instructor to be assigned,
        capacity (int): capacity Maximum capacity of this class 
    """
    course: Course = Course(className, year, capacity)
    courseInstructors[course] = instructorName


def changeCapacity(className: str, year: int, capacity: int):
    """[summary]

    Args:
        className (str): Name of the class for which capacity should be changed
        year (int): Year in which this class is taught
        capacity (int): New capacity of this class, must be at least equal to the number of students enrolled
    """

    course: Optional[Course] = findCourse(className, year)
    if not course is None:
        course.capacity = capacity


def classExists(className: str, year: int) -> bool:
    """REturn True if class exists. 
    Args:
        className (str): Classname
        year (int): Year

    """
    return findCourse(className, year) != None


def getClassInstructor(className: str, year: int) -> Optional[str]:
    course: Optional[Course] = findCourse(className, year)
    if course is None:
        return None
    return courseInstructors[course]


def getClassCapacity(className: str, year: int) -> int:
    """Return the Capacity of the class
    """
    course: Optional[Course] = findCourse(className, year)
    if course is None:
        return -1
    return course.capacity
