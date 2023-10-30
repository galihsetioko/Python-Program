
import json

class Paraphrase():
    def start(self):
        print("paraphrase running..")
    def getPhrase(self, text):
        result = []
        with open('dictionary\data', 'r') as file:
            dictionary = json.load(file)
        text_split = text.split()
        for i in text_split:
            if dictionary.get(i) != None:
                result.append(dictionary.get(i))
            else:
                result.append(i)
        return " ".join(result)