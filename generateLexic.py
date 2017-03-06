lexic = {}
with open("corpus.txt", "r") as ins:
    for line in ins:
    	content = line.split()
    	word = content[0]
    	tag = content[1]

        if lexic.has_key(word):
            if lexic[word].has_key(tag):
                lexic[word][tag] += 1
            else:
                lexic[word][tag] = 1
        else:
            lexic[word] = {}
            lexic[word][tag] = 1   

print "ok"

lexicfile = open("lexic.txt","w") 
for p in lexic.keys():
    for t in lexic[p]:
        ocurrencia = lexic[p][t]
        newline = '%s %s %d \n' % (p, t, ocurrencia)
        lexicfile.write(newline)