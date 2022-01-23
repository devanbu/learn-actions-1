import src.DataManager as DataManager
import src.Admin as Admin
import src.Instructor as Instructor
import src.Student as Student
import unittest


class TestAdmin(unittest.TestCase):

    def test_nocourse(self):
        Admin.resetAll()
        self.assertIsNone(DataManager.findCourse("ecs999", 2022))

    def test_newcourse(self):
        Admin.resetAll()
        Admin.createClass("ecs160", 2022, "Prem Devanbu", 101)
        crs: Course = DataManager.findCourse("ecs160", 2022)
        self.assertIsNotNone(crs)
        self.assertEqual(DataManager.courseInstructors[crs],  "Prem Devanbu")

    def test_newEnrollee(self):
        Admin.resetAll()
        Admin.createClass("ecs160", 2022, "Prem Devanbu", 101)
        Student.registerForClass("Evil Keneval", "ecs160", 2022)
        self.assertTrue(Student.isRegisteredFor(
            "Evil Keneval", "ecs160", 2022))


class TestStudent(unittest.TestCase):

    # Crap, this resetAll() method is called everywhere to reset the
    # the data to a clean state for testing. Can we get rid of repeating
    # code and put it in one place?

    def test_studentaddscoursetwice(self):
        Admin.resetAll()
        Admin.createClass("ecs160", 2022, "Prem Devanbu", 101)
        count: int = Admin.getClassCapacity("ecs160", 2022)
        self.assertEqual(count, 101)
        Student.registerForClass("Evil Keneval", "ecs160", 2022)
        count: int = Admin.getClassCapacity("ecs160", 2022)
        self.assertEqual(count, 100)


class TestHomework(unittest.TestCase):

    def test_newhomework(self):
        Admin.resetAll()
        Admin.createClass("ecs160", 2022, "Prem Devanbu", 101)
        crs: DataManager.Course = DataManager.findCourse("ecs160", 2022)
        crs.addHomework(DataManager.Homework("HW1"))
        self.assertIsNotNone(crs.getHomework("HW1"))
