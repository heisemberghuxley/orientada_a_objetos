class Animals:
    def __init__(self, dog, cat, lion, elephant):
        self.dog = dog
        self.cat = cat
        self.lion = lion
        self.elephant = elephant
        self.have_bones = True
        
    def what_are_they(self):
        self.vertebrates_are_walking = False
        print(f"Vertebrate animals are characterized by having bones.")
        
    def stood_up(self):
        self.these_are_vertebrates = True
        print(f"An example of this are:\ndogs: {self.dog}\ncats: {self.cat}\nlions: {self.lion}\n{self.elephant}\nand many more animals.")
        
animals = Animals("dogs", "cats", "lions", "elephants who are afraid of mice")
animals.what_are_they()
print()
animals.stood_up()

# (---------------------------------------------------)
# inheritance
class Invertebrates(Animals):
    def __init__(self, dog, cat, lion, elephant, arthropods, mollusks, echinoderms):
        super().__init__(dog, cat, lion, elephant)
        self.arthropods = arthropods
        self.mollusks = mollusks
        self.echinoderms = echinoderms
        
    def name_some(self):
        print(f"An arthropod animal would be: {self.arthropods}\nAn example of a mollusk would be: {self.mollusks}\nAnd of an echinoderm would be: {self.echinoderms}")
        
    def end_topic(self):
        print(f"These would be some examples of the many types and classes of invertebrate animals that exist.")
        
without_bones = Invertebrates("dogs", "cats", "lions", "elephants who are afraid of mice", "a spider", "an octopus", "a starfish")

without_bones.name_some()
print()
without_bones.end_topic()










