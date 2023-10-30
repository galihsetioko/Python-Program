from . import paraphrase

class InterpreterArea():
    def __init__(self):
        self.pr = paraphrase.Paraphrase()
        
    def start(self):
        print('\n')
        print('-'*20)
        ask = True
        while ask:
            get_input = input("> ")
            if get_input == "exit":
                ask = False
            print(self.pr.getPhrase(get_input))