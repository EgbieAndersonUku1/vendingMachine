
class Calculate(object):

    def __init__(self, first_val, second_val):
        self.first_val = first_val
        self.second_val = second_val

    def calculate(self):
        return round((self.first_val - self.second_val), 2)