class car:
  def __init__(self,model:str,year:int):
    self.model=model
    self.year=year
  def auto(self):
    return f'the {self.model} is {self.year}' 

  car1 = car()
  car1.auto()
