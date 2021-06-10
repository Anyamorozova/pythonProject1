class Date:
  
    date = None
    
    def __init__(self, date):
      Date.date = date
      
    @classmethod  
    def get_int_to_date(cls):
      lst_date = cls.date.split('-')
      for el in lst_date:
        print(int(el))
    
    @staticmethod    
    def validation_date():
      lst_date = Date.date.split('-')
      if 1 <= int(lst_date[0]) <= 31 and 1 <= int(lst_date[1]) <= 12:
        print("Validation succses!")
      else:
        print("Validation failed!")

      
Date("20-03-2020").get_int_to_date()      
date_1 = Date("21-13-2020")
date_1.validation_date()
Date("22-03-2020").validation_date()
