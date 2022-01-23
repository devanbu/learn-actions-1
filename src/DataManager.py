class Enrollee:
    pass


class Homework:
    pass


class Course:
    def __init__(self, name: str, year: int, capacity: int) -> None:
        self.name = name
        self.year = year
        self.capacity = capacity
        self.homeworks = set()
        self.enrollees = set()

    def addStudent(self, new_un: Enrollee):
        self.enrollees.add(new_un)

    def removeStudent(self, the_un: Enrollee):
        self.enrollees.remove(the_un)

    def getEnrollees(self) -> set:
        return self.enrollees

    def addHomework(self, homework: Homework):
        self.homeworks.add(homework)

    def getHomework(self, name: str) -> Homework:
        for hw in self.homeworks:
            if hw.name == name:
                return hw
        return None


class Enrollee:
    def __init__(self, name: str):
        self.courses = set()
        self.name = name

    def getName(self):
        return self.name

    def addCourse(self, course: Course):
        self.courses.add(course)

    def dropCourse(self, course: Course):
        self.courses.remove(course)

    def equals(self, other: any) -> bool:
        if (other == None):
            return false
        if (not isinstance(other, Enrollee)):
            return false
        return other.getName() == self.name


# This is the Data Manager code
enrollees: set[Enrollee] = set()
courseInstructors: dict[Course, str] = dict()


def findCourse(name: str, year: int) -> Course:
    for crs in courseInstructors.keys():
        if(crs.name == name and crs.year == year):
            return crs
    return None


def findStudent(name: str) -> Enrollee:
    for s in enrollees:
        if s.name == name:
            return s
    new_un = Enrollee(name)
    enrollees.add(new_un)
    return new_un


def reset():
    enrollees.clear()
    courseInstructors.clear()

# This is the end of the DataManager code.


class Homework:
    def __init__(self, name: str):
        self.name = name
        self.studentSubmissions = dict()
        self.studentGrades = dict()

    def getName(self):
        return self.name

    def submit(self, enrollee: Enrollee, solution: str):
        self.studentSubmissions[enrollee] = solution

    def gradeStudent(self, enrollee: Enrollee, grade: int):
        self.studentGrades[enrollee] = grade

    def getSubmission(self, enrollee: Enrollee):
        return self.studentSubmissions[enrollee]

    def getGrade(self, enrollee: Enrollee):
        return self.studentGrades[enrollee]

    def equals(self, other):
        if other is None:
            return false
        if not (isinstance(other, Homework)):
            return false
        return Homework(other).name == self.name
