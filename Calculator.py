#!/usr/bin/env python

#This should probably be made a function eventually that takes arguments for slope, Yint, frag length, and dilution factor

OutFile = open('output.txt', 'w')

def Concentration_pM(d_factor,ct,Yint,slope,frag):
   result = (d_factor*(10**((float(ct)-Yint)/float(slope)))*(452/float(frag)))
   return result
def Concentration_uguL(concentration_pM,frag):
    result = ((concentration_pM)*(10**-15)*frag*617.9*10**6)
    return result

#Header for output file
OutFile.write('Sample\tConcentration(pM)\tConcentration(ug/uL)\n')

#The lists for this loop are undefine, needs to be joined with Dan's code to work
PMs = []
uguL = []
for index in range(len(Samples)):
    PMs.append(Concentration_pM(100000,ct_mean[index],11,-3.3,248))
for value in PMs:
    uguL.append(Concentration_uguL(value,248))
for index in range(len(Samples)):
   OutFile.write('%s\t%d\t%d\n' % (Samples[index],PMs[index],uguL[index])) 

OutFile.close()
