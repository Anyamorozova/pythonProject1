from abc import ABC, abstractmethod

class Clothes(ABC):
  
    title = None
    
    def __init__(self, title):
      self.title = title
      
    @abstractmethod
    def fabric_consumption(self):
        pass


class Сoat(Clothes):
  
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size
        
    @property    
    def fabric_consumption(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
  
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height
        
    @property    
    def fabric_consumption(self):
        return self.height * 2 + 0.3
        
        
coat = Сoat("coat",42)
print(coat.fabric_consumption)
suit = Suit("suit",164)
print(suit.fabric_consumption)
print(f"Общий подсчет расхода ткани: {coat.fabric_consumption + suit.fabric_consumption}")
