class Beverages:
    def __init__(self, soda, tea, alcohol_free_wine):
        self.soda = soda
        self.tea = tea
        self._alcohol_free_wine = alcohol_free_wine
        
    def satisfy(self):
        self.these_beverages_satisfy = True
        print(f"{self.soda} apple, {self.tea}, and {self._alcohol_free_wine} are tasty.")
        
    def consume(self):
        self.cannot_consume_in_excess = False
        print("But they should not be consumed excessively for health reasons.")
        
    def get_alcohol_free_wine(self):
        return self._alcohol_free_wine
    
    def set_alcohol_free_wine(self, alcohol_free_wine):
        self._alcohol_free_wine = alcohol_free_wine
        

# Inheritance (---------------------------)
class Consumables(Beverages):
    def __init__(self, soda, tea, alcohol_free_wine, juices, yogurts):
        super().__init__(soda, tea, alcohol_free_wine)
        self.juices = juices
        self.yogurts = yogurts
        
    def drink(self):
        print(f"{self.juices} are healthier than other consumable products.")
        
    def consume(self):
        print(f"{self.yogurts} is a dairy product rich in flavor.")
        

purchase = Consumables("apple-flavored soda", "sun tea", "D1", "juices", "yogurt")
purchase.drink()
print()
purchase.consume()
print()

beverages = Beverages("soda", "sun tea", "alcohol-free wine")
print()
beverages.satisfy()
print()
beverages.consume()
print()
beverages.set_alcohol_free_wine("wine")
print(beverages.get_alcohol_free_wine())

