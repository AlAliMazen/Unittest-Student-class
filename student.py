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
        
