def logger(func):
    def logging():
        print("Function execution started")
        func()
        print("Function execution end")
    return logging

@logger
def calc():
    print(5*5)

calc()