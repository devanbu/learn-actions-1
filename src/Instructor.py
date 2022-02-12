from src.DataManager import *

def addHomework(instructorName, className, year, homework):
    course = findCourse(className, year)
    if not course is None:
        course.addHomework(Homework(homework))

def assignGrade(instructorName, className, year, hwName, stuName, grade):
    the_un = findStudent(stuName)
    course = findCourse(className, year)
    if not the_un is None and (not course is None):
        homework = course.getHomework(hwName)
        if not homework is None:
            homework.gradeStudent(the_un, grade)

def homeworkExists(clName, year, hwName):
    course = findCourse(clName, year)
    if course is None:
        return False
    return not course.getHomework(hwName) is None

def getGrade(clName, year, hwName, stuName):
    course = findCourse(clName, year)
    the_un = findStudent(stuName)
    if course is None or the_un is None:
        return None
    hw = course.getHomework(hwName)
    if hw is None:
        return None
    return hw.getGrade(the_un)
