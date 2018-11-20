import datetime
class CalcController(object):
    
    @staticmethod
    def start():
        while True:
            CalcView.print_menu()
            operation = CalcView.inp_operation()
            if operation is None:
                print("Invalid argument")
                continue
            if operation == 5:
                exit()

            operands = CalcView.inp_operands()
            if operands is None:
                print("Invalid operand")
                continue

            try:
                result = CalcModel.start_calc(operation, operands[0], operands[1])
                CalcView.print_result(result)
            except ZeroDivisionError:
                print("Zero division error")


class CalcModel(object):
    
    def log(func):
        def wrap_log(*args, **kwargs):
            f = open('log.log', 'a')
            ar = str(args)
            res = str(func(*args, **kwargs))
            f.write(datetime.datetime.now().isoformat() + ' вызвана функция ' + func.__name__ + ' с аргументами ' + ar + ' и результатом ' + res + ' \n')
            f.close()
            
            return func(*args, **kwargs)
    
        return wrap_log
    
    @staticmethod
    def start_calc(operation, op1, op2):
        if operation == 1:
            return CalcModel.add(op1, op2)
        elif operation == 2:
            return CalcModel.sub(op1, op2)
        elif operation == 3:
            return CalcModel.mult(op1, op2)
        elif operation == 4:
            return CalcModel.div(op1, op2)

    @staticmethod       
    @log
    def add(op1, op2):
        return op1 + op2

    @staticmethod
    @log
    def sub(op1, op2):
        return op1 - op2

    @staticmethod
    @log
    def mult(op1, op2):
        return op1 * op2

    @staticmethod
    @log
    def div(op1, op2):
        return op1 / op2


class CalcView(object):
    @staticmethod
    def print_menu():
        print("""
               1. +
               2. -
               3. *
               4. /
               5. exit""")

    @staticmethod
    def inp_operation():
        try:
            return int(input("Input: "))
        except:
            return None

    @staticmethod
    def inp_operands():
        try:
            op1 = int(input("operand 1: "))
            op2 = int(input("operand 2: "))
            return [op1, op2]
        except:
            return None

    @staticmethod
    def print_result(result):
        print("Result: " + str(result))

 


if __name__ == "__main__":
    CalcController.start()
