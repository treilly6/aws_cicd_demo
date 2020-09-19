from Errors import OddEvenError

class OddOrEven:
    def __init__(self, number):
      self.number = None
      self.set_number(number)
      print(f"{number} is {self.parity}")

    def set_number(self, number):
      if type(number) != int:
        raise OddEvenError(number)
      else:
        self.number = number

    @property
    def parity(self):
      if self._isEven():
        return "EVEN"
      else:
        return "ODD"

    def _isEven(self):
      remainder = self.number % 2

      if remainder == 0:
        return True
      else:
        return False
