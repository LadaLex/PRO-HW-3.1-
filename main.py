class NegativeNumberException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
    def get_exception_massage(self):
        return self.message

while True:
    try:
        number = float(input("Input price: "))
        if number < 0:
            raise NegativeNumberException("Negative number price")
        break
    except ValueError:
        print("ValueError: Only integers acceptable")
    except NegativeNumberException as err:
            print(err.get_exception_massage())