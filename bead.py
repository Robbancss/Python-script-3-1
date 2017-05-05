import os.path

class Ford:
    "Translater class."
    def __init__(self, vocab):
        self.fromWord = vocab.keys()
        self.toWord = vocab.values()
    def fordit(self, fromTranslate, toTranslate):
        if os.path.isfile(fromTranslate):
            ls = []
            with open(fromTranslate, mode='r') as fromfile:
                ls = fromfile.read
                for line in fromfile:
                    print(line)
        else:
            print("Nincs input file!")
