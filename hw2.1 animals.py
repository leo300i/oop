class Animal:

    def __init__(self, animals, voicetext):
        self.animals = animals
        self.voicetext = voicetext

    def comand_voice(self):
        print(f"{self.animals} {self.voicetext}")


dog = Animal('dog:', 'гафгаф')
dog.comand_voice()

cow = Animal('cow:', 'муууу')
cow.comand_voice()

cat = Animal('cat:', 'мяу')
cat.comand_voice()

bear = Animal('bear:', 'aрррр')
bear.comand_voice()