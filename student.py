# import the header for time and date
from datetime import date, timedelta


class Student:
    """
    A Student class as base for method testing
    """
    
    def __init__(self, first_name, last_name):
        
        # we use underscore before the attribute to indicate it is read only function
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today()+timedelta(days=365) # this line doesn't take care of leap year
        self.naughty_list = False

    # in order to make this method a read only method , we have to add the decorative @ property
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
    """

    steps to solve the challenge
    - create a new test method called test_apply_extension
    - Inside test_apply_extension, store the current end_date for our student instance in a variable called old_end_date
    - Call a method named apply_extension that will take a number od days as an argument on the student instance to update the end_date
    - Assert the instance's end_date equals the old end date plus the says argument that was passed in the using timedelta
    - Rin the tests to confirm that the new method is failing
    - Om the student class, create a new method called apply_extension that has a parameter called days
    - Use the timedelta method from datetime to update the end_date property
    - Run the tests to confirm they are working
    """
    def apply_extension(self, period):
        self.end_date = self.end_date+timedelta(days=period)
        
