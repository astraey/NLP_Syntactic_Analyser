import time
import sys
import unicodedata
import random

start_time = time.time()

def main():
    primerPas()
    segonPas()
    tercerPas()
    print("[INFO] --- Total seconds %s ---" % (time.time() - start_time))


def strip_accents(s):
    # nos comemos el char con accento -- se puede afinar mas
    return (s.decode('unicode_escape').encode('ascii','ignore'))

def primerPas():
    print "[INFO] Primer pas"
    
    """
    Primer pas: Generacio del Model del Llenguatge El primer pas consisteix
    a escriure un programa que, donat un corpus anotat (en el nostre cas,
    el fitxer corpus.txt), escrigui en un fitxer la informacio dels tags i les paraules
    trobades. El fitxer s'anomenara lexic.txt i cada linia ha de contenir la
    informacio (paraula, tag, ocurrencies) separada per tabuladors.

    cantado Adj 443
    cantado V 325
    cantados Adj 13
    ...

    """

    sys.stdout.write("[INFO] Leyendo corpus.txt ............... ")
    sys.stdout.flush()

    lexic = {}
    with open("corpus.txt", "r") as ins:
        for line in ins:
            line = line.decode("latin_1").encode("UTF-8")
            content = line.split()
            word = content[0].lower()
            tag = content[1]

            if lexic.has_key(word):
                if lexic[word].has_key(tag):
                    lexic[word][tag] += 1
                else:
                    lexic[word][tag] = 1
            else:
                lexic[word] = {}
                lexic[word][tag] = 1  


    sys.stdout.write("DONE\n")

    sys.stdout.write("[INFO] Generando lexic.txt .............. ")
    sys.stdout.flush()

    lexicfile = open("lexic.txt","w") 
    for w in lexic.keys():
        for t in lexic[w]:
            ocurrencia = lexic[w][t]
            newline = '%s\t%s\t%d\n' % (w, t, ocurrencia)
            lexicfile.write(newline)

    sys.stdout.write("DONE\n")


def getLexicDic():

    sys.stdout.write("[INFO] Leyendo lexic.txt ................ ")
    sys.stdout.flush()

    lexicDic_ = {}
    with open("lexic.txt", "r") as fichero:
        for linea in fichero:
            linea = linea.decode("latin_1").encode("UTF-8").split()
            # linea[0] = word, linea[1] = tag, linea[2] = ocurrencia
            ww = strip_accents( linea[0].lower() )
            if not lexicDic_.has_key(ww):
                lexicDic_[ ww ] = {}
            lexicDic_[ ww ][ linea[1] ] = linea[2]

    sys.stdout.write("DONE\n")
    return lexicDic_


def etiquetatge(filename,lexicDic):

    sys.stdout.write("[INFO] Etiquetando " + filename + " ........... ")
    sys.stdout.flush()

    newfilename = "tagged_" + filename
    newfile = open(newfilename,"w") 

    tags = ["Adv", "Int", "Punt", "Data", "VAux", "Fin", "NC", "Det", "Pron", "Abr", "Num", "V", "NP", "Conj", "Adj", "Prep"]
    
    with open(filename, "r") as f:
        for line_ in f:
            tag_ = random.choice(tags)
            token_ = line_.decode("latin_1").encode("UTF-8").lower().split()[0]
            token = strip_accents( token_ )
            if lexicDic.has_key(token):
                occ_, tag_ = max((lexicDic[token][i],i) for i in lexicDic[token])
            
            newfile.write(token_ + "\t" + tag_ + "\n")

    sys.stdout.write("DONE\n")


def segonPas():
    print "[INFO] Segon pas"
    """
    Segon pas: Etiquetatge d'un corpus utilitzant un Model del Llenguatge. 
    Per a completar aquesta part de la practica s'ha d'implementar un programa 
    que utilitzant el Model del Llenguatge generat a l'apartat anterior etiqueti 
    els fitxers test_1.txt i test_2.txt
    """
    dic = getLexicDic()
    etiquetatge("test_1.txt",dic)
    etiquetatge("test_2.txt",dic)




def getFileContent(filename):

    sys.stdout.write("[INFO] Leyendo " + filename + "................ ")
    sys.stdout.flush()

    fileContent = {}
    with open(filename, "r") as fichero:
        for linea in fichero:
            linea = linea.decode("latin_1").encode("UTF-8").split()
            # linea[0] = word, linea[1] = tag
            ww = strip_accents( linea[0].lower() )
            fileContent[ ww ] = linea[1]

    sys.stdout.write("DONE\n")
    return fileContent

def calcultateTest(numTest):

    text = getFileContent("tagged_test_" + numTest + ".txt")
    gold_standard = getFileContent("gold_standard_" + numTest + ".txt")

    correctos = 0

    for i in text.keys():
        if text[i] == gold_standard[i]:
            correctos += 1

    porcentaje = float(correctos) / float(len(text))

    print "[INFO] Porcentaje test " + numTest + ":  " , round(porcentaje,2) * 100 , "%"


def tercerPas():
    print "[INFO] Tercer pas"
    """
    Tercer pas: Avaluacio dels resultats El tercer pas consisteix a avaluar els
    resultats del programa. Per a aixo cal escriure un programa que compari els resultats
    del nostre etiquetatge amb l'etiquetatge correcte. Aquests resultats correctes
    es troben als fitxers gold_standard_1.txt i gold_standard_2.txt.
    Aquests fitxers son la referencia; si el programa etiquetes totes les paraules del
    text correctament, els resultats coincidirien 100 por cien amb el gold standard. El
    programa ha de comparar els dos resultats i indicar el percentatge de correccio
    """
    
    calcultateTest("1")
    calcultateTest("2")

    

if __name__ == "__main__":
    main()