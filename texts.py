class Texts:
    def __init__(self, information, language, evolution):
        self.information = information
        self.language = language
        self.evolution = evolution
        
    def learn(self):
        print(f"Thanks to texts, we can access {self.information} that allow us to educate ourselves.")
    
    def obtain(self):
        print(f"We can receive our first {self.language}, which is very important for communication and the {self.evolution} of humanity.")
        
letters = Texts("information", "language", "advancement")
print()
letters.learn()
print()
letters.obtain()

class Books(Texts):
    def __init__(self, information, language, evolution, knowledge, self_learning):
        super().__init__(information, language, evolution)
        self.knowledge = knowledge
        self.self_learning = self_learning
        
    def memorize(self):
        print(f"Thanks to the {self.knowledge} provided by texts, we can memorize important information.")
        
    def retain(self):
        print(f"We can also obtain good {self.self_learning}.")
        
documentation = Books("information", "language", "advancement", "knowledge", "self-learning")
print()
documentation.memorize()
print()
documentation.retain()
print()
