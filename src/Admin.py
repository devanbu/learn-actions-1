from src.DataManager import *



def createClass(className, year, instructorName, capacity):
    """Creates a new class

    Args:
        className (str): Name of the class/course
        year (int): year Calendar year in which the course is to be taught
        instructorName (str): instructorName Name of instructor to be assigned,
        capacity (int): capacity Maximum capacity of this class 
    """
    course = Course(className, year, capacity)
    courseInstructors[course] = instructorName

def changeCapacity(className, year, capacity):
    """[summary]

    Args:
        className (str): Name of the class for which capacity should be changed
        year (int): Year in which this class is taught
        capacity (int): New capacity of this class, must be at least equal to the number of students enrolled
    """
    course = findCourse(className, year)
    if not course is None:
        course.capacity = capacity

def classExists(className, year):
    """REturn True if class exists. 
    Args:
        className (str): Classname
        year (int): Yea

    """
    return findCourse(className, year) != None

def getClassInstructor(className, year):
    course = findCourse(className, year)
    if course is None:
        return None
    else:
        return courseInstructors[course]

def getClassCapacity(className, year):
    """Return the Capacity of the class
    """
    course = findCourse(className, year)
    if course is None:
        return -1
    else:
        return course.capacity
