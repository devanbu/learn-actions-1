from src.DataManager import *

def registerForClass(stuName, clName, year):
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        the_un.addCourse(course)
        course.addStudent(the_un)
        return
    return

def dropClass(stuName, clName, year):
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        the_un.addCourse(course)
        course.removeStudent(the_un)
    return

def submitHomework(stuName, hwName, answer, clName, year):
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        hw = course.getHomework(hwName)
        if not hw is None:
            hw.submit(the_un, answer)

def isRegisteredFor(stuName, clName, year):
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        return the_un in course.getEnrollees()
    return False

def hasSubmitted(stuName, hwName, clName, year):
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        hw = course.getHomework(hwName)
        if not hw is None:
            return not hw.getSubmission(the_un) is None
    return False
