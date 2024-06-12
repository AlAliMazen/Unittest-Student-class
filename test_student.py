import unittest
from student import Student

# we need to import the timedelta 
from datetime import timedelta


class TestStudent(unittest.TestCase):
    """
    whenever a unit test method is run, two python methods run before and after the test
    both these functions must be written with camelCase and make use of the self keyword.

    When looking at the test beneath, we can see that there is some kind of repeating
    the code by the need of creating an instance of the class every time.

    setUp method will be called before the test and 
    tearDown method will be called after the test is done


    there is also a possibility to call the function setUp and tearDown only once 
    this use case is important for the creating of Database and populating it with 
    data

    in order to make use of this functionality we have to stick to the syntax
    1- add a decorator of @classmethod 
    2- add cls as parameter of both methods
    3- use camelCase when writing method

    """
    @classmethod
    def setUpClass(cls):
        print("Set up class method")

    @classmethod
    def tearDownClass(cls):
        print("Tear down class method")


    def setUp(self):
        print("Set Up method")
        self.student=Student("John","Doe")
    
    def tearDown(self):
        # id does nothing but destroy any objects and connections to the database
        print("Tear Down method")

    # first we have to create an instance of student class inside the test function
    # first unittest for the function 
    def test_full_name(self):
        print("test fullname method")
        #student = Student("John", "Doe") # no need for this line anymore because we created the object in the setUp 
        self.assertEqual(self.student.full_name, "John Doe")
    
    # second test will check when we call a method from student class called alert santa which should sit the attribute naughty to True
    def test_alert_santa(self):
        print("test alert santa method")
        #student = Student("John", "Doe")
        self.student.alert_santa()
        # we should see that the attribute should be turned to True when method is called
        self.assertTrue(self.student.naughty_list)
    
    # test the email method if it return students'email address as firstname.lastname@email.compile
    def test_student_email(self):
        print("test student mail")
        #student = Student("John", "Doe")
        self.assertEqual(self.student.email,"john.doe@email.com")

    # test a method of apply_extension method whether it modifies the the end_date attributes
    def test_apply_extension(self):
        print("Apple extension date")
        # store student current end date in a variable
        old_end_date = self.student.end_date

        #call the function 
        self.student.apply_extension(5)
        
        # use assert equal to compare
        self.assertEqual(self.student.end_date, old_end_date+timedelta(days=5))


if __name__ == '__main__':
    unittest.main()