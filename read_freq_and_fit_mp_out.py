import re
import math
import tempfile

# define function_1
# loadfile *.log for gaussian
# x is the input name without type
def loadfile(x):
    f = open (x+'.out', 'r')
    nameout2 = f.read()
    freqo = nameout2[nameout2.find(' Frequencies dumped to record'):nameout2.find('Zero point energy')]
    f.close()
    return (freqo)

# define function_2
# save lists to the file, because frequencies and intensities are kept in lists
# x is the save name; y is the input name; z and w are two lists
def savefile(x,y,z,w):
    f2 = open (x+'_'+y, 'w+') 
    slx =' '.join([repr(v).strip('\'') for v in z])
    sly =' '.join([repr(v).strip('\'') for v in w])
    s = slx +'\r'+sly  
    f2.write(s)
    f2.close()
    return()

# define function_3
# fetch the frequency or intensity and output valuse from loaded .log file
# a is loaded file; x is the start string of each lines; y is the end string
def fetchstr(a,x,y,z):
    n = a.count(x)
    listf = [[]]*(n)
    listf2 = [[]]*n*2
    listf2[0] = a
    for i in range(0, n-1 +1):
        listf[i] = listf2[i][listf2[i].find(x)+15:listf2[i].find(y)]
        listf2[i+1]= listf2[i][listf2[i].find(z)+10:]
    listff =' '.join([repr(v).strip('\'') for v in listf])
    p = re.compile(r'\s+')
    listff_2 = p.split(listff)
    nn = len(listff_2)
    listfff = [[]]*(nn-1)
    for j in range(0, nn-2 +1):
        listfff[j] = listff_2[j+1]
    return(listfff)
# finish define funcions

# main-1 fetch the frequencies and fit the spectra with lorentz type
print('input the file name:')
iname = input("-->");
print('input the spectra range:')
xstart = int(input("-->"));
xend = int(input("-->"));

freqo = loadfile(iname)
fetchfqx = fetchstr(freqo,'Wavenumbers [','\n Intensities [km/mol]','Intensities [relative]')
fetchIty = fetchstr(freqo,'Intensities [km/mol]','\n Intensities [relative]','Intensities [relative]')

n_1 = len(fetchfqx)+1
n_2 = int((xend - xstart)/2)+1
fitx = [[]]*n_2
fity = [[]]*n_2
fitt = [[]]*n_2*(n_1+1)
fitt[0]=0

for i in range(0, n_2-1 +1):
    fitx[i] = xstart + i*2
    for j in range(1,n_1-1 +1):
        fitt[i*n_1+j] = float(fitt[i*n_1+j-1]) + ((float(fitx[i]) - float(fetchfqx[j-1]))**2+8**2)**(-1)*8*float(fetchIty[j-1]) 
    fity[i] = fitt[n_1*(i+1)-1]
    fitt[n_1*(i+1)] = int(0)
    
savefile('freqir',iname,fetchfqx,fetchIty)
savefile('freqfit',iname,fitx,fity)
# finish main
