This is a program that works to paraphrase sentences.

Paraphrase is 
This program has 2 modes, namely interpreter and command line mode. The user can choose
between the two modes. The default mode is [interpreter].

The way to use it is:

python main.py -h / -c -f filename -o outputfile

-h          To display a help message
-c          Flags to enter command line mode 
-f          Contains the path of the file to be paraphrased
-o          Contains the output filename for the paraphrased file

The program uses the json dictionary file as data to paraphrase.
The dictionary file contains a collection of verbs with their synonyms, Making the writing inputted by the user
more unique and reduce the percentage of plagiarism.

Dictionary can currently only be used in Indonesian.

Note: In the tools folder there is also a program to help users add the desired verbs
automatically and directly converted in json format