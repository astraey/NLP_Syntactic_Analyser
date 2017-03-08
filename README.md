<h1># P1_CIPL</h1>

<h3>Run</h3>

<b>$ python main.py</b>

<h3>Primer pas</h3>

Generacio del Model del Llenguatge El primer pas consisteix
a escriure un programa que, donat un corpus anotat (en el nostre cas,
el fitxer corpus.txt), escrigui en un fitxer la informacio dels tags i les paraules
trobades. El fitxer s'anomenara lexic.txt i cada linia ha de contenir la
informacio (paraula, tag, ocurrencies) separada per tabuladors.

cantado Adj 443<br>
cantado V 325<br>
cantados Adj 13<br>
...<br>

<b>$ python generateLexic.py</b>

<h3>Segon pas</h3>

Etiquetatge d'un corpus utilitzant un Model del Llenguatge. 
Per a completar aquesta part de la practica s'ha d'implementar un programa 
que utilitzant el Model del Llenguatge generat a l'apartat anterior etiqueti 
els fitxers test_1.txt i test_2.txt

<h3>Tercer pas</h3>

Avaluacio dels resultats El tercer pas consisteix a avaluar els
resultats del programa. Per a aixo cal escriure un programa que compari els resultats
del nostre etiquetatge amb l'etiquetatge correcte. Aquests resultats correctes
es troben als fitxers gold_standard_1.txt i gold_standard_2.txt.
Aquests fitxers son la referencia; si el programa etiquetes totes les paraules del
text correctament, els resultats coincidirien 100 por cien amb el gold standard. El
programa ha de comparar els dos resultats i indicar el percentatge de correccio