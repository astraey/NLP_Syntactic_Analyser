import sys
import string
from collections import namedtuple



def main():

    if sys.argv[1] == "-createLexic":
        print "Creating lexic..."

        CreateLexic()


        print "The Lexic have been created successfully and stored in lexic.txt"
    else:
        print "Invalid argument. Please execute the command: 'python main.py -createLexic' to create the file lexic.txt"


def CreateLexic():

    corpus = open("corpus.txt", "r")
    lexid = {}
    lexic = open("lexic.txt", "w")

    for linec in corpus:
        linec = linec.decode("latin_1").encode("UTF-8")

        linec = linec.replace("\r\n", "")
        linec = linec.replace('\n', '')
        wordsc = linec.split("\t")
        # print wordsc

        if wordsc[0] in lexid:
            if wordsc[1] in lexid[wordsc[0]]:
                lexid[wordsc[0]][wordsc[1]] += 1
            else:
                lexid[wordsc[0]] = {wordsc[1]: 1}
        else:
            lexid[wordsc[0]] = {wordsc[1]: 1}

    # print lexid

    for key1 in lexid:
        for key2 in lexid[key1]:
            lexic.write(key1 + "\t" + key2 + "\t" + str(lexid[key1][key2]) + "\n")




if __name__ == "__main__":
    main()

