import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('logs/employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

''' Simple file handler log '''

class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

        logger.info("Created Employee - {} {}".format(self.fullname,self.email))


    @property
    def email(self):
        return "{}.{}@email.com".format(self.first.lower(),self.last.lower())


    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)



emp_1 = Employee('Vasya','Pupkin')
emp_2 = Employee('Anatoliy','popov')    




