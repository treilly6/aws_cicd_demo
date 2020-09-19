class OddEvenError(Exception):
    def __init__(self, number):
      self.message = f'Expected type int but instead got type {type(number)}'
      self.number = number
      super().__init__(self.message)

    def __str__(self):
      return f'{self.number} is invalid type ---> {self.message}'
