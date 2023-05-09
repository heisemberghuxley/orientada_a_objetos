class Celestials:
    def __init__(self, stars, sun, moon):
        self.stars = stars
        self._sun = sun
        self.moon = moon
        self.are_celestial_bodies = True
        
    def shine(self):
        self.all_appear_at_the_same_time = False
        print(f"The stars: {self.stars} and are situated in outer space.")
        
    def describe(self):
        self.are_visible = True
        print(f"The sun: {self._sun} is in outer space and can be observed from Earth.\nThe moon always {self.moon} is a natural satellite.")
        
    def get_sun(self):
        return self._sun
    def set_sun(self,sun):
        self._sun = sun
        
space = Celestials("are bodies that shine in the distance","rises every day", "rises at night")
print()
space.shine()
print()
space.describe()
space.set_sun("fire")
print(space.get_sun())

# (---------------------------------------------------)
# inheritance

class Planets(Celestials):
    def __init__(self, sun, stars, moon, mercury, jupiter):
        super().__init__(sun, stars, moon)
        self.mercury = mercury
        self.jupiter = jupiter
        
    def description(self):
        print(f"{self.mercury}: is the closest planet to the Sun in the solar system and the smallest.")
        
    def description2(self):
        print(f"{self.jupiter} is the largest planet in the solar system and the fifth in order of distance from the Sun.")
        
worlds = Planets("sun","stars","moon","mercury","jupiter")
print()
worlds.description()
print()
worlds.description2()

