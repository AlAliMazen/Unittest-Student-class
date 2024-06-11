import unittest
from student import Student


class TestStudent(unittest.TestCase):
    # first we have to create an instance of student class inside the test function
    # first unittest for the function 
    def test_full_name(self):
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")
    
    # second test will check when we call a method from student class called alert santa which should sit the attribute naughty to True
    def test_alert_santa(self):
        student = Student("John", "Doe")
        student.alert_santa()
        # we should see that the attribute should be turned to True when method is called
        self.assertTrue(student.naughty_list)
    
    # test the email method if it return students'email address as firstname.lastname@email.compile
    def test_student_email(self):
        student = Student("John", "Doe")
        self.assertEqual(student.email,"john.doe@email.com")



if __name__ == '__main__':
    unittest.main()