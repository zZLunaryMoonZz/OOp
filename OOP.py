from typing import Literal
class Animal:
    def __init__(self,
                 animal_type:str,
                 animal_noises:str,
                 feeding:Literal ["травоядное", "хищное", "всеядное"]
                 ):
        self.animal_type = animal_type
        self.animal_noises = animal_noises
        self.feeding = feeding

    def __str__(self)->str:
        return f"Это {self.feeding} животное {self.animal_type}."
    
cat = Animal ("Кот", "мяу", "всеядное")
giraf = Animal ("жираф", "х-ы-ы", "травоядное")
hyena = Animal("гиена", "м-у-у-у-в", "хищное")

print (cat, cat.sound())
print (giraf, giraf.sound())
print (hyena, hyena.sound())