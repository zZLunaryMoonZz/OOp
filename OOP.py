from typing import Literal
class Animal:
    def __init__(
            self,
            animal_type:str,
            animal_noises:str,
            animal_sound:str,
            feeding:Literal ["травоядное", "хищное", "всеядное"]
                ):
        self.animal_type = animal_type
        self.animal_noises = animal_noises
        self.animal_sound = animal_sound
        self.feeding = feeding

    def __str__(self)->str:
        return f"Это {self.feeding} животное {self.animal_type}."
    def sound(self) -> str:
        return f"{self.animal_type} издает следующие звуки {self.animal_noises}."
    
cat = Animal ("Кот", "мяу", "всеядное")
giraf = Animal ("жираф", "х-ы-ы", "травоядное")
hyena = Animal("гиена", "м-у-у-у-в", "хищное")

print (cat, cat.sound())
print (giraf, giraf.sound())
print (hyena, hyena.sound())