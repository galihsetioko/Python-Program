This is a program for saving simple financial reports in json format
this program uses Command Line Interface to receive input from the user.

How to use : 

filename.py -f [filename.json] --income [20000] --description ["Description Here"]

-f, --filename     Input the location of the json file
-i, --income       Tells the program to put data into the dictionary "income"
-o, --outcome      Tells the program to put data into the "outcome" dictionary
-d, --description  Label or give information about "what your money was used to buy"

Use only one of the arguments between --income or --outcome, do not use both at once.

The program will detect the input entered according to the date when it was run, when you run the
program with the same json file tomorrow, the program will automatically change the date information in the json file.
By creating a new label according to the current date.
