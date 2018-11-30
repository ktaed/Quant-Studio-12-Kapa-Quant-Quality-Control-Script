#!/usr/bin/env python

OutFile = open('output.txt', 'w')

def Concentration_pM(d_factor,ct,Yint,slope,frag):
   result = (d_factor*(10**((float(ct)-Yint)/float(slope)))*(452/float(frag)))
   return result
def Concentration_uguL(concentration_pM,frag):
    result = ((concentration_pM)*(10**-15)*frag*617.9*10**6)
    return result

#Examples to verify math
#pm = Concentration_pM(100000,30,11,-3.3,248)
#print(pm)
#print(Concentration_uguL(pm,248))

OutFile.write('Sample\tConcentration(pM)\tConcentration(ug/uL)\n')
#OutFile.write(%s'\t'%d'\t'%d) % (Samples,PM,uguL)
#OutFile.write('test')

PMs = []
uguL = []
for index in range(len(Samples)):
    PMs.append(Concentration_pM(100000,ct_mean[index],11,-3.3,248))
for value in PMs:
    uguL.append(Concentration_uguL(value,248))
for index in range(len(Samples)):
   OutFile.write('%s\t%d\t%d\n' % (Samples[index],PMs[index],uguL[index])) 

OutFile.close()
