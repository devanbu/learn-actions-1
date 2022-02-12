from typing import Set
from typing import Dict
from typing import Optional
from typing import Any
from typing import cast

#class Enrollee:
#    pass


#class Homework:
#    pass


class Course:
    def __init__(self, name: str, year: int, capacity: int ) -> None:
        self.name = name
        self.year = year
        self.capacity = capacity
        self.homeworks: Set[Homework] = set()
        self.enrollees: Set[Enrollee]= set()

    def addStudent(self, new_un: Enrollee)->None:
        self.enrollees.add(new_un)

    def removeStudent(self, the_un: Enrollee) -> None:
        self.enrollees.remove(the_un)

    def getEnrollees(self) -> Set[Enrollee]:
        return self.enrollees

    def addHomework(self, homework: Homework) -> None:
        self.homeworks.add(homework)

    def getHomework(self, name: str) -> Optional[Homework]:
        hw: Homework
        for hw in self.homeworks:
            if hw.getName() == name:
                return hw
        return None


class Enrollee:
    def __init__(self, name: str):
        self.courses: Set[Course] = set()
        self.name = name

    def getName(self) -> str:
        return self.name

    def addCourse(self, course: Course) -> None:
        self.courses.add(course)

    def dropCourse(self, course: Course) -> None:
        self.courses.remove(course)

    def equals(self, other: Any) -> bool:
        if (other == None):
            return False
        if (not isinstance(other, Enrollee)):
            return False
        return cast(Homework,other).getName() == self.name


# This is the Data Manager code
enrollees: set[Enrollee] = set()
courseInstructors: dict[Course, str] = dict()


def findCourse(name: str, year: int) -> Optional[Course]:
    for crs in courseInstructors.keys():
        if(crs.name == name and crs.year == year):
            return crs
    return None


def findStudent(name: str):
    for s in enrollees:
        if s.name == name:
            return s
    new_un = Enrollee(name)
    enrollees.add(new_un)
    return new_un


def reset() -> None:
    enrollees.clear()
    courseInstructors.clear()

# This is the end of the DataManager code.


class Homework:
    def __init__(self, name: str):
        self.name = name
        self.studentSubmissions : Dict[Enrollee,str] = dict()
        self.studentGrades :Dict[Enrollee,int]= dict()

    def getName(self) -> str :
        return self.name

    def submit(self, enrollee: Enrollee, solution: str) -> None:
        self.studentSubmissions[enrollee] = solution

    def gradeStudent(self, enrollee: Enrollee, grade: int) :
        self.studentGrades[enrollee] = grade

    def getSubmission(self, enrollee: Enrollee) :
        return self.studentSubmissions[enrollee]

    def getGrade(self, enrollee: Enrollee):
        return self.studentGrades[enrollee]

    def equals(self, other : Any) -> bool:
        if other is None:
            return False
        if not (isinstance(other, Homework)):
            return False
        return other.name == self.name
