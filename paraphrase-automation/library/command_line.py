from . import paraphrase


class CommandLineArea():
    def __init__(self, filename, output):
        self.filename = filename
        self.output = output
        self.pr = paraphrase.Paraphrase()
    def start(self):
        result = []
        with open(self.filename) as file:
            buff = file.readlines()
        for i in buff:
            a = i
            if a.endswith('\n'):
                a = a.replace('\n','')
                temp = self.pr.getPhrase(a)
                result.append(temp)
                
            else:
                temp = self.pr.getPhrase(a)
                result.append(temp)
                # result.append(a)
        
        print(result)
        with open(self.output, 'w') as file:
            to_line = "\n".join(result)
            file.write(to_line)