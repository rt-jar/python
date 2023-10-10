context = dict(age=25)
def contextCreator(funct):
    def createContext(*param):
        global context
        context["name"] = "Lakhan"
        funct(param[0], param[1])
    return createContext

def contextPrinter(funct):
    def printContext(*param):
        print(context)
        funct(param[0], param[1])
    return printContext

@contextCreator
@contextPrinter
def contextManipulator(first, second):
    print("in")
    print(context.get("name"))
    print(first + "   " + second)

contextManipulator("Calculator", "Vishnoi")