import os

class File:
    def __init__(self, location):
        self.location = location
    
    def exceptionHandler(func):
        def handle(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(e)
                raise e

        return handle


        

    @exceptionHandler
    def create(self):
        try:
            f = open(self.location, "wt")
            return f
        except Exception as e:
            print(e)
        else:
            print("File created successfully")
   
    @exceptionHandler
    def read(self):
        f = open(self.location, "rt")
        return f.read()
   
    @exceptionHandler
    def delete(self):
        if os.path.exists(self.location):
            os.remove(self.location)
        else:
            print(f"{self.location} file doesn't exist")


file = File("/Users/ratneshsingh/Downloads/test/test1/test1.txt")
fp = file.create()
if fp:
    fp.writelines(["Test test"])
    fp.close()
    print(file.read())



#file.delete()

