'''
# loadfile *.log or *.out for gaussian/molpro
# Frequencies and thermochem is the start and end of the vibration section
'''

def loadfile(x):
    f = open (x, 'r')
    nameout2 = f.read()
    freqo = nameout2[nameout2.find('Frequencies --'):nameout2.find('- Thermochemistry -')]
    f.close()
    return (freqo)

'''
 fetch the frequency or intensity and output valuse in listff
 a is input string
 x is the start of each raw; y is the end; and z move to next
'''

def fetchstr(a,x,y,z):
    n = a.count(x)
    listf = [[]]*(n)
    listf2 = [[]]*n*2
    listf2[0] = a
    for i in range(0, n-1 +1):
        listf[i] = listf2[i][listf2[i].find(x)+15:listf2[i].find(y)]
        listf2[i+1]= listf2[i][listf2[i].find(z)+10:]
    listff =' '.join([repr(v).strip('\'') for v in listf])
    return(listff)

'''
 save ordered frequency and intensity to the file
'''

def savefile(x,y):
    f2 = open (x, 'w+') 
    f2.write(y)
    f2.close()
    return()

'''
then is the main coding
'''

print('input the file name:')
iname = input("-->");

freqo = loadfile(iname)

listall = fetchstr(freqo,'Frequencies','\n Red.','Atom')+'\r'+fetchstr(freqo,'IR Inten','\n  Atom','Atom')

print(listall)

savefile('freqir',listall)

