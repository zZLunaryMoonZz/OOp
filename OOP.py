from typing import Literal
class Animal:
    def __init__(
            self,
            animal_type: str,
            animal_sound: str,
            feeds: Literal ["травоядное", "хищное", "всеядное"]
                ):
        self.animal_type = animal_type
        self.feeds = feeds
        self.animal_sound = animal_sound

    def __str__(self)->str:
        return f'Это {self.feeds} животное {self.animal_type}!'

    def sound(self) -> str:
        return f'{self.animal_type} издает звуки {self.animal_sound}!'

    def feed(self) -> str:
        return f'{self.animal_type} кушает {self.feeds}!'

    
cat = Animal ("Кот", "мяу", "всеядное")
print (cat, cat.sound())
print (cat, cat.feed())

giraf = Animal ("жираф", "х-ы-ы", "травоядное")
print (giraf, giraf.sound())
print (giraf, giraf.feed())

hyena = Animal("гиена", "м-у-у-у-в", "хищное")
print (hyena, hyena.sound())
print (hyena, hyena.feed())
