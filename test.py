class Laptop:
  def __init__(self, pro, ram, prices):
    self.__processor = pro
    self.__ram = ram
    self.__prices = prices

  def set_processor(self, pro):
    self.__processor = pro

  def set_ram(self, ram):
    self.__ram = ram

  def set_prices(self, prices):
    self.__prices = prices

  def get_processor(self):
    return self.__processor

  def get_ram(self):
    return self.__ram

  def get_prices(self):
    return self.__prices

class Dell (Laptop):
  def __init__(self, pro, ram, prices):
    Dell.__init__(self, pro, ram, prices)
    