import argparse
from library.command_line import CommandLineArea
from library.interpreter import InterpreterArea

class Mainapp():
    def __init__(self):
        parser = argparse.ArgumentParser()
        # parser.add_argument('-i', '--interpreter', action='store_true', help='Enter mode interpr
        parser.add_argument('-c', '--command',action='store_true', help='Mode CLI [ Default mode : interpreter ]')
        parser.add_argument('-f','--file', help='File to paraphrase')
        parser.add_argument('-o', '--output',help='Output filename')
        self.args = parser.parse_args()
        # if self.args.command == True:
        #     self.args = parser.parse_args()
    def enterMode(self):
        if self.args.command == True:
            cl = CommandLineArea(self.args.file, self.args.output)
            cl.start()
        else :
            ip = InterpreterArea()
            ip.start()
            

if __name__ == '__main__':
    mainapp = Mainapp()
    mainapp.enterMode()
