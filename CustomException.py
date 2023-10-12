class EmployeeNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


def exceptionTest(threshold):
    try:
        print("Started")
        if threshold > 5 : 
            raise EmployeeNotFoundException("Employee not found")
    except EmployeeNotFoundException as e:
        print(e)
    

exceptionTest(10)