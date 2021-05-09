class Laptop:
  def __init__(self, pro, ram, price):
    self.__processor = pro
    self.__ram = ram
    self.__price = price

  def set_processor(self, pro):
    self.__processor = pro

  def set_ram(self, ram):
    self.__ram = ram

  def set_price(self, price):
    self.__price = price

  def set_standard_mouse(self, mouse):
    self.__standard_mouse = mouse

  def set_standard_laptopcase(self, case):
    self.__standard_laptopcase = case

  def set_standard_sdcard(self, sdcard):
    self.__standard_sdcard = sdcard

  def get_processor(self):
    return self.__processor

  def get_ram(self):
    return self.__ram

  def get_price(self):
    return self.__price

  def get_standard_mouse(self):
    return self.__standard_mouse 

  def get_standard_laptopcase(self):
    return self.__standard_laptopcase

  def get_standard_sdcard(self):
   return self.__standard_sdcard 

class Dell (Laptop):
  def __init__(self, pro, ram, price):
    Dell.__init__(self, pro, ram, price)

class HP (Laptop):
  def __init__(self, pro, ram, price):
    Dell.__init__(self, pro, ram, price)
    
class Lenovo (Laptop):
  def __init__(self, pro, ram, price):
    Dell.__init__(self, pro, ram, price)
    